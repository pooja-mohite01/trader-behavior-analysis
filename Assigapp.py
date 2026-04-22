import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile


st.set_page_config(layout="wide", page_title="Trader Analysis Dashboard")

st.title("Trader Behavior and Performance Analysis")

# -----------------------------

# Load Data

# -----------------------------

@st.cache_data
def load_data():
    merged_df = pd.read_csv("C:/Users/Ravindra/Downloads/merged_data.csv", parse_dates=['date'])
    trader_metrics = pd.read_csv("C:/Users/Ravindra/Downloads/trader_metrics.csv")
    return merged_df, trader_metrics
merged_df, trader_metrics = load_data()

# -----------------------------

# Create required metrics

# -----------------------------

daily_pnl = merged_df.groupby(['account', 'date'])['closed_pnl'].sum().reset_index()

win_rate = merged_df.groupby('account')['closed_pnl'].apply(lambda x: (x > 0).mean()).reset_index(name='win_rate')

avg_trade_size = merged_df.groupby('account')['size_usd'].mean().reset_index()

trades_per_day = merged_df.groupby('date').size().reset_index(name='trade_count')

long_short_ratio = merged_df['side'].value_counts(normalize=True)

win_rate_sentiment = merged_df.groupby('sentiment')['closed_pnl'].apply(lambda x: (x > 0).mean()).reset_index(name='win_rate')

loss_analysis = merged_df[merged_df['closed_pnl'] < 0].groupby('sentiment')['closed_pnl'].mean().reset_index(name='avg_negative_pnl')

avg_trades_per_sentiment = merged_df.groupby(['date', 'sentiment']).size().reset_index(name='count')
avg_trades_per_sentiment = avg_trades_per_sentiment.groupby('sentiment')['count'].mean().reset_index(name='average_daily_trades')

long_short_bias = merged_df.groupby(['sentiment', 'side']).size().unstack(fill_value=0)
long_short_bias = long_short_bias.apply(lambda x: x / x.sum(), axis=1).reset_index()

avg_position_size_sentiment = merged_df.groupby('sentiment')['size_usd'].mean().reset_index(name='average_position_size_usd')

# -----------------------------

# Sidebar Navigation

# -----------------------------

selected_section = st.sidebar.radio("Go to", [
"Key Metrics Analysis",
"Performance by Sentiment",
"Behavior by Sentiment",
"Trader Segmentation"
])

# -----------------------------

# Key Metrics

# -----------------------------

if selected_section == "Key Metrics Analysis":
    st.header("1. Key Metrics Analysis")
    st.dataframe(daily_pnl)
    st.dataframe(win_rate)
    st.dataframe(avg_trade_size)
    fig, ax = plt.subplots()
    sns.lineplot(x='date', y='trade_count', data=trades_per_day, ax=ax)
    st.pyplot(fig)
    st.write(long_short_ratio)

elif selected_section == "Performance by Sentiment":
    st.header("2. Performance by Sentiment")
    fig, ax = plt.subplots()
    sns.barplot(x='sentiment', y='win_rate', data=win_rate_sentiment, ax=ax)
    st.pyplot(fig)
    fig, ax = plt.subplots()
    sns.barplot(x='sentiment', y='avg_negative_pnl', data=loss_analysis, ax=ax)
    st.pyplot(fig)

# -----------------------------

# Behavior Analysis

# -----------------------------

elif selected_section == "Behavior by Sentiment":
    st.header("3. Behavior by Sentiment")
    fig, ax = plt.subplots()
    sns.barplot(x='sentiment', y='average_daily_trades', data=avg_trades_per_sentiment, ax=ax)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    melted = long_short_bias.melt(id_vars='sentiment', var_name='side', value_name='ratio')
    sns.barplot(x='sentiment', y='ratio', hue='side', data=melted, ax=ax)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.barplot(x='sentiment', y='average_position_size_usd', data=avg_position_size_sentiment, ax=ax)
    st.pyplot(fig)

# -----------------------------

# Trader Segmentation

# -----------------------------

elif selected_section == "Trader Segmentation":
    st.header("4. Trader Segmentation")

    features = ['win_rate', 'size_usd', 'total_trades']

    st.subheader("Cluster Summary")
    cluster_summary = trader_metrics.groupby('cluster')[features].mean()
    st.dataframe(cluster_summary)

    st.subheader("Trader Clusters Visualization")

    pairplot = sns.pairplot(trader_metrics, vars=features, hue='cluster')
    st.pyplot(pairplot.fig)

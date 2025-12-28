import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Expense Dashboard", layout="wide")
st.title("💰 Japanese Bank Expense Tracker")

uploaded_file = st.file_uploader("Upload your expense CSV", type=["csv"])

if uploaded_file is not None:
    # 1. Load Data with Japanese Encoding
    # Try 'shift_jis' or 'utf-8-sig' depending on how your bank exports it
    try:
        df = pd.read_csv(uploaded_file, encoding='shift_jis')
    except:
        df = pd.read_csv(uploaded_file, encoding='utf-8-sig')

    # 2. Data Cleaning
    # Convert date to datetime objects
    df['年月日'] = pd.to_datetime(df['年月日'])
    
    # Clean the Withdrawal column (fill empty with 0)
    df['お引出し'] = df['お引出し'].fillna(0)
    
    # Filter only rows where money was spent (Withdrawals > 0)
    df_expenses = df[df['お引出し'] > 0].copy()

    # Show the raw data if requested
    if st.checkbox("Show raw data"):
        st.write(df_expenses)

    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filters")
    month_list = df_expenses['年月日'].dt.strftime('%Y-%m').unique()
    selected_month = st.sidebar.multiselect("Select Month(s)", options=month_list, default=month_list)
    
    # Apply filter
    mask = df_expenses['年月日'].dt.strftime('%Y-%m').isin(selected_month)
    filtered_df = df_expenses[mask]

    # --- VISUALIZATIONS ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Spending by Transaction Name")
        # We group by 'お取り扱い内容' to sum up repeated shops (like Facebook or Inageya)
        fig_pie = px.pie(filtered_df, values='お引出し', names='お取り扱い内容', 
                         title='Where is the money going?')
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        st.subheader("Daily Spending Trend")
        # Sum expenses by day
        daily_df = filtered_df.groupby('年月日')['お引出し'].sum().reset_index()
        fig_line = px.line(daily_df, x='年月日', y='お引出し', title='Daily Spending')
        st.plotly_chart(fig_line, use_container_width=True)

    # Bar Chart for specific items
    st.subheader("Top Expenses (Ranked)")
    top_expenses = filtered_df.groupby('お取り扱い内容')['お引出し'].sum().sort_values(ascending=False).reset_index()
    fig_bar = px.bar(top_expenses, x='お取り扱い内容', y='お引出し', color='お引出し',
                     title='Total Spent per Merchant')
    st.plotly_chart(fig_bar, use_container_width=True)

else:
    st.info("Please upload your bank CSV file (Shift-JIS encoded) to get started.")
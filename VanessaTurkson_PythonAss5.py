# ============================================================
#  VANESSA TURKSON – PYTHON ASSIGNMENT 5
#  FULL STREAMLIT DASHBOARD WITH QUESTIONS 1–4
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Juice Sales Dashboard", layout="wide")

# ============================
# APP TITLE & FILE UPLOADER
# ============================
st.title("🍊 Juice & Smoothie Sales Analytics Dashboard")
st.write("Prepared by: **Vanessa Turkson**")

uploaded_file = st.file_uploader("Upload the Juice Sales Excel File (ejb.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Convert date early for Question 2 & 4
    df["Date Ordered"] = pd.to_datetime(df["Date Ordered"])

    # ============================================================
    # QUESTION 1: CATEGORY SALES COMPARISON
    # ============================================================
    st.header("Question 1: Compare Sales Performance of Juices vs Smoothies")

    # Group sales by Category
    sales_by_category = df.groupby("Category")["$ Sales"].sum()

    st.subheader("Total Sales by Category")
    st.write(sales_by_category)

    # Bar chart
    fig1, ax1 = plt.subplots()
    ax1.bar(sales_by_category.index, sales_by_category.values, color=["orange", "green"])
    ax1.set_title("Total Sales: Juices vs Smoothies")
    ax1.set_xlabel("Category")
    ax1.set_ylabel("Total Sales ($)")
    ax1.grid(axis="y", linestyle="--", alpha=0.4)

    st.pyplot(fig1)

    st.subheader("Interpretation (Q1)")
    if sales_by_category["Juices"] > sales_by_category["Smoothies"]:
        st.write("Juices generate **more revenue** than Smoothies.")
    elif sales_by_category["Juices"] < sales_by_category["Smoothies"]:
        st.write("Smoothies generate **more revenue** than Juices.")
    else:
        st.write("The two categories generate **the same revenue**.")

    st.markdown("---")

    # ============================================================
    # QUESTION 2: SALES OVER TIME (LINE CHART)
    # ============================================================
    st.header("Question 2: Sales Over Time (Daily Trend)")

    # Group by day
    daily_sales = df.groupby("Date Ordered")["$ Sales"].sum()

    st.subheader("Daily Total Sales")
    st.write(daily_sales)

    # Line chart
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(daily_sales.index, daily_sales.values, marker="o")
    ax2.set_title("Daily Sales Trend Over Time")
    ax2.set_xlabel("Date Ordered")
    ax2.set_ylabel("Total Sales ($)")
    ax2.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(rotation=45)

    st.pyplot(fig2)

    st.subheader("Interpretation (Q2)")
    st.write("""
        The time-series chart shows fluctuations in daily sales.
        Peaks represent high-revenue days, while dips indicate periods of lower activity.
        This helps identify seasonal patterns and high-performing days.
    """)

    st.markdown("---")

    # ============================================================
    # QUESTION 3: SATISFACTION RATING DISTRIBUTION
    # ============================================================
    st.header("Question 3: Service Satisfaction Rating Distribution")

    # Select ratings & drop missing
    ratings = df["Service Satisfaction Rating"].dropna()
    rating_counts = ratings.value_counts().sort_index()

    st.subheader("Customer Rating Counts")
    st.write(rating_counts)

    # Bar chart
    fig3, ax3 = plt.subplots()
    ax3.bar(rating_counts.index, rating_counts.values, color="skyblue")
    ax3.set_title("Service Satisfaction Rating Distribution")
    ax3.set_xlabel("Rating (1 = Poor, 5 = Excellent)")
    ax3.set_ylabel("Number of Customers")
    ax3.grid(axis="y", linestyle="--", alpha=0.4)

    st.pyplot(fig3)

    st.subheader("Interpretation (Q3)")
    st.write("""
        The chart visualizes customer satisfaction levels.
        Higher bars indicate the most frequent ratings.
        This helps assess overall service quality and identify improvement areas.
    """)

    st.markdown("---")

    # ============================================================
    # QUESTION 4 (BONUS): TABS DASHBOARD
    # ============================================================
    st.header("Question 4 (Bonus): Full Dashboard with Tabs")

    tab1, tab2, tab3 = st.tabs([
        "Category Sales",
        "Sales Over Time",
        "Satisfaction Ratings"
    ])

    # -------------------- TAB 1 --------------------
    with tab1:
        st.subheader("Category Sales Comparison")
        st.write(sales_by_category)

        fig_tab1, ax_tab1 = plt.subplots()
        ax_tab1.bar(sales_by_category.index, sales_by_category.values, color=["orange", "green"])
        ax_tab1.set_title("Sales by Category")
        ax_tab1.set_xlabel("Category")
        ax_tab1.set_ylabel("Total Sales ($)")
        st.pyplot(fig_tab1)

    # -------------------- TAB 2 --------------------
    with tab2:
        st.subheader("Daily Sales Trend")
        fig_tab2, ax_tab2 = plt.subplots(figsize=(10, 5))
        ax_tab2.plot(daily_sales.index, daily_sales.values, marker="o")
        ax_tab2.set_title("Daily Sales Trend")
        ax_tab2.set_xlabel("Date Ordered")
        ax_tab2.set_ylabel("Total Sales ($)")
        st.pyplot(fig_tab2)

    # -------------------- TAB 3 --------------------
    with tab3:
        st.subheader("Service Satisfaction Ratings")
        fig_tab3, ax_tab3 = plt.subplots()
        ax_tab3.bar(rating_counts.index, rating_counts.values, color="skyblue")
        ax_tab3.set_title("Service Satisfaction Ratings")
        ax_tab3.set_xlabel("Rating")
        ax_tab3.set_ylabel("Count")
        st.pyplot(fig_tab3)

else:
    st.info("Please upload the ejb.xlsx dataset to continue.")

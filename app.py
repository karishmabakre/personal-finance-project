import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# PAGE CONFIGURATION
st.set_page_config(
    page_title="FinSight - Personal Finance",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CUSTOM CSS
st.markdown("""
<style>

/*APPLICATION*/

.stApp {
    background: #f5f7fb;
}

.block-container {
    padding-top: 1.4rem;
    padding-bottom: 2rem;
}


/*MAIN HEADER */

.main-header {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    padding: 30px 32px;
    border-radius: 22px;
    color: white;
    margin-bottom: 24px;
    box-shadow: 0 10px 28px rgba(15, 23, 42, 0.10);
}

.main-header h1 {
    margin: 0;
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -0.6px;
}

.main-header p {
    margin: 7px 0 0;
    color: #dbeafe;
    font-size: 15px;
}


/* SIDEBAR - MODERN FINANCE EXPLORER */

[data-testid="stSidebar"] {
    background:
        radial-gradient(
            circle at top right,
            rgba(37, 99, 235, 0.14),
            transparent 35%
        ),
        linear-gradient(
            180deg,
            #071321 0%,
            #0b1929 55%,
            #081522 100%
        ) !important;

    border-right: 1px solid rgba(148, 163, 184, 0.25);
}

[data-testid="stSidebar"] > div:first-child {
    padding: 0.75rem 0.8rem 1.5rem;
}

[data-testid="stSidebar"] * {
    font-family: Arial, sans-serif;
}


/* SIDEBAR HEADER */

.finance-header {
    padding: 17px 15px 20px;
    margin: -3px -3px 10px;
    border-bottom: 1px solid rgba(148, 163, 184, 0.27);
}

.finance-header-inner {
    display: flex;
    align-items: center;
    gap: 13px;
}

.finance-logo {
    width: 53px;
    height: 53px;
    min-width: 53px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 14px;
    background: linear-gradient(135deg, #8b5cf6, #3b82f6);
    color: white;
    font-size: 29px;
    font-weight: 800;
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.25);
}

.finance-title {
    color: #f8fafc;
    font-size: 24px;
    font-weight: 800;
    letter-spacing: -0.4px;
    line-height: 1.15;
}

.finance-subtitle {
    color: #cbd5e1;
    font-size: 12.5px;
    margin-top: 5px;
    line-height: 1.35;
}


/* FILTER HEADINGS */

.filter-heading {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 18px;
    margin-bottom: 7px;
}

.filter-name {
    color: #f8fafc;
    font-size: 16px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 9px;
}

.filter-icon {
    width: 24px;
    min-width: 24px;
    text-align: center;
    font-size: 20px;
}

.filter-actions {
    color: #cbd5e1;
    font-size: 18px;
    white-space: nowrap;
}

.info-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #cbd5e1;
    color: #172033;
    font-size: 12px;
    font-weight: 800;
}


/* MULTISELECT CONTROL */

[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background: rgba(30, 41, 59, 0.82) !important;
    border: 1px solid rgba(148, 163, 184, 0.25) !important;
    border-radius: 12px !important;
    min-height: 48px;
    box-shadow: none !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
    border-color: rgba(96, 165, 250, 0.60) !important;
    box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.08) !important;
}

[data-testid="stSidebar"] div[data-baseweb="select"] input {
    color: #e2e8f0 !important;
}


/* SELECTED CHIPS - NO RED */

[data-testid="stSidebar"] div[data-baseweb="tag"] {
    background: linear-gradient(135deg, #f1f7ff, #dbeafe) !important;
    border: 1px solid rgba(96, 165, 250, 0.32) !important;
    border-radius: 9px !important;
    padding: 4px 7px !important;
    margin: 3px 3px 3px 0 !important;
    color: #0759c7 !important;
}

[data-testid="stSidebar"] div[data-baseweb="tag"] span {
    color: #0759c7 !important;
    font-size: 13.5px !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] div[data-baseweb="tag"] svg {
    fill: #0759c7 !important;
    color: #0759c7 !important;
    width: 17px;
    height: 17px;
}


/* DROPDOWN MENU */

div[data-baseweb="popover"] {
    background: #111f31 !important;
    border: 1px solid rgba(148, 163, 184, 0.25) !important;
    border-radius: 12px !important;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.35) !important;
}

div[data-baseweb="popover"] li {
    color: #e2e8f0 !important;
    background: transparent !important;
}

div[data-baseweb="popover"] li:hover {
    background: rgba(59, 130, 246, 0.18) !important;
}

[data-testid="stSidebar"] div[data-baseweb="select"] svg {
    color: #cbd5e1 !important;
    fill: #cbd5e1 !important;
}


/* Hide Streamlit's duplicate widget labels because
   custom filter headings are displayed above them. */

[data-testid="stSidebar"] .stMultiSelect label {
    display: none !important;
}


/* SLIDER */

[data-testid="stSidebar"] [data-testid="stSlider"] {
    padding: 2px 3px 8px;
}

[data-testid="stSidebar"] [data-testid="stSlider"] [role="slider"] {
    background: #3b82f6 !important;
    border: 3px solid #eef6ff !important;
    box-shadow: 0 0 0 1px rgba(59, 130, 246, 0.35);
}

[data-testid="stSidebar"] [data-testid="stSlider"] p {
    color: #cbd5e1 !important;
}


/* CHECKBOX */

[data-testid="stSidebar"] [data-testid="stCheckbox"] {
    padding: 12px 7px 7px;
    margin-top: 4px;
    border-top: 1px solid rgba(148, 163, 184, 0.24);
}

[data-testid="stSidebar"] [data-testid="stCheckbox"] label {
    color: #f8fafc !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}


/* DIVIDER */

.filter-divider {
    height: 1px;
    background: rgba(148, 163, 184, 0.24);
    margin: 17px 0 7px;
}


/* MAIN KPI CARDS */

.kpi-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 20px;
    min-height: 104px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.kpi-title {
    color: #64748b;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.4px;
}

.kpi-value {
    color: #111827;
    font-size: 27px;
    font-weight: 800;
    margin-top: 8px;
}


/* SECTION TITLES */

.section-title {
    font-size: 24px;
    font-weight: 750;
    color: #111827;
    margin-top: 27px;
    margin-bottom: 14px;
}


/* FOOTER */

.footer {
    text-align: center;
    color: #64748b;
    padding: 25px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# LOAD AND CLEAN DATA
@st.cache_data
def load_data():
    """Load the finance dataset and perform basic cleaning."""

    file_path = "dataset/missing_personal.csv"
    data = pd.read_csv(file_path)

    # Remove exact duplicate rows.
    data = data.drop_duplicates().copy()

    # Amount must be numeric for calculations and filtering.
    data["Amount"] = pd.to_numeric(
        data["Amount"],
        errors="coerce"
    )

    if data["Amount"].isna().all():
        raise ValueError("The Amount column does not contain valid numeric values.")

    data["Amount"] = data["Amount"].fillna(
        data["Amount"].median()
    )

    # Date processing.
    if "Date" in data.columns:
        data["Date"] = pd.to_datetime(
            data["Date"],
            errors="coerce"
        )
        data["Month_Number"] = data["Date"].dt.month
        data["Day_Number"] = data["Date"].dt.dayofweek
    else:
        data["Month_Number"] = np.nan
        data["Day_Number"] = np.nan

    # Fill missing categorical values with the mode.
    categorical_columns = [
        "Description",
        "Category",
        "PaymentMethod",
        "Location",
        "AccountType",
        "TransactionType",
        "DeviceUsed",
        "Currency",
        "MerchantType",
        "LoyaltyProgram",
        "Weekday",
        "Month",
        "TimeOfDay"
    ]

    for column in categorical_columns:
        if column in data.columns:
            mode_value = data[column].mode(dropna=True)
            if not mode_value.empty:
                data[column] = data[column].fillna(mode_value.iloc[0])

    return data


# DATASET

try:
    df = load_data()
except FileNotFoundError:
    st.error(
        "Dataset not found. Put 'missing_personal.csv' inside the 'dataset' folder."
    )
    st.stop()
except ValueError as error:
    st.error(str(error))
    st.stop()


# MAIN HEADER
st.markdown("""
<div class="main-header">
    <h1>💰 FinSight</h1>
    <p>Your simple personal finance dashboard</p>
    <p>Track spending • Explore transactions • Understand your habits</p>
</div>
""", unsafe_allow_html=True)


# SIDEBAR HEADER
st.sidebar.markdown("""
<div class="finance-header">
    <div class="finance-header-inner">
        <div class="finance-logo">↗</div>
        <div>
            <div class="finance-title">Finance Explorer</div>
            <div class="finance-subtitle">
                Interactive filtering from your dataset
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# CATEGORY FILTER
st.sidebar.markdown("""
<div class="filter-heading">
    <div class="filter-name">
        <span class="filter-icon">📁</span>
        Category
    </div>
    <div class="filter-actions">
        <span class="info-icon">i</span>&nbsp;⌄
    </div>
</div>
""", unsafe_allow_html=True)

categories = sorted(
    df["Category"].dropna().astype(str).unique()
)

selected_categories = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories,
    key="category_filter"
)


# PAYMENT METHOD FILTER
st.sidebar.markdown("""
<div class="filter-heading">
    <div class="filter-name">
        <span class="filter-icon">💳</span>
        Payment Method
    </div>
    <div class="filter-actions">
        <span class="info-icon">i</span>&nbsp;⌄
    </div>
</div>
""", unsafe_allow_html=True)

payment_methods = sorted(
    df["PaymentMethod"].dropna().astype(str).unique()
)

selected_payment = st.sidebar.multiselect(
    "Payment Method",
    payment_methods,
    default=payment_methods,
    key="payment_filter"
)


# LOCATION FILTER
st.sidebar.markdown("""
<div class="filter-heading">
    <div class="filter-name">
        <span class="filter-icon" style="color:#a855f7;">📍</span>
        Location
    </div>
    <div class="filter-actions">
        <span class="info-icon">i</span>&nbsp;⌄
    </div>
</div>
""", unsafe_allow_html=True)

locations = sorted(
    df["Location"].dropna().astype(str).unique()
)

selected_locations = st.sidebar.multiselect(
    "Location",
    locations,
    default=locations,
    key="location_filter"
)


# TRANSACTION TYPE FILTER
st.sidebar.markdown("""
<div class="filter-heading">
    <div class="filter-name">
        <span class="filter-icon" style="color:#34d399;">⇄</span>
        Transaction Type
    </div>
    <div class="filter-actions">
        <span class="info-icon">i</span>&nbsp;⌄
    </div>
</div>
""", unsafe_allow_html=True)

transaction_types = sorted(
    df["TransactionType"].dropna().astype(str).unique()
)

selected_transaction = st.sidebar.multiselect(
    "Transaction Type",
    transaction_types,
    default=transaction_types,
    key="transaction_filter"
)


# TIME OF DAY FILTER
st.sidebar.markdown("""
<div class="filter-heading">
    <div class="filter-name">
        <span class="filter-icon" style="color:#fbbf24;">🕐</span>
        Time of Day
    </div>
    <div class="filter-actions">
        <span class="info-icon">i</span>&nbsp;⌄
    </div>
</div>
""", unsafe_allow_html=True)

time_values = sorted(
    df["TimeOfDay"].dropna().astype(str).unique()
)

selected_time = st.sidebar.multiselect(
    "Time of Day",
    time_values,
    default=time_values,
    key="time_filter"
)


# AMOUNT RANGE FILTER
st.sidebar.markdown("""
<div class="filter-heading">
    <div class="filter-name">
        <span class="filter-icon" style="color:#fbbf24;">💰</span>
        Amount Range
    </div>
    <div class="filter-actions">
        <span class="info-icon">i</span>
    </div>
</div>
""", unsafe_allow_html=True)

minimum_amount = float(df["Amount"].min())
maximum_amount = float(df["Amount"].max())

amount_range = st.sidebar.slider(
    "Amount Range",
    min_value=minimum_amount,
    max_value=maximum_amount,
    value=(minimum_amount, maximum_amount),
    key="amount_filter"
)


# HIGH EXPENSE FILTER
st.sidebar.markdown(
    '<div class="filter-divider"></div>',
    unsafe_allow_html=True
)

high_expenses = st.sidebar.checkbox(
    "🔥 Only High Expenses (> ₹5,000)",
    key="high_expense_filter"
)


# APPLY ALL FILTERS
filtered_df = df[
    df["Category"].isin(selected_categories)
    & df["PaymentMethod"].isin(selected_payment)
    & df["Location"].isin(selected_locations)
    & df["TransactionType"].isin(selected_transaction)
    & df["TimeOfDay"].isin(selected_time)
    & df["Amount"].between(amount_range[0], amount_range[1])
].copy()

if high_expenses:
    filtered_df = filtered_df[filtered_df["Amount"] > 5000]


# NO DATA CHECK
if filtered_df.empty:
    st.warning("No transactions match your selected filters.")
    st.info(
        "Try selecting more options or increasing the amount range."
    )
    st.stop()


# BASIC CALCULATIONS
total_spending = filtered_df["Amount"].sum()
transaction_count = len(filtered_df)
average_transaction = filtered_df["Amount"].mean()
highest_transaction = filtered_df["Amount"].max()


# KPI CARDS
st.markdown(
    '<div class="section-title">📊 Your Spending at a Glance</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">TOTAL SPENDING</div>
            <div class="kpi-value">₹{total_spending:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">TRANSACTIONS</div>
            <div class="kpi-value">{transaction_count:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">AVERAGE TRANSACTION</div>
            <div class="kpi-value">₹{average_transaction:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">HIGHEST TRANSACTION</div>
            <div class="kpi-value">₹{highest_transaction:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# QUICK SUMMARY
st.markdown(
    '<div class="section-title">✨ Quick Summary</div>',
    unsafe_allow_html=True
)

category_spending = (
    filtered_df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

location_spending = (
    filtered_df.groupby("Location")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

payment_spending = (
    filtered_df.groupby("PaymentMethod")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_category = category_spending.index[0]
top_category_amount = category_spending.iloc[0]
top_location = location_spending.index[0]
top_payment = payment_spending.index[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        f"🏆 **Top Spending Category**\n\n"
        f"**{top_category}**\n\n"
        f"₹{top_category_amount:,.0f}"
    )

with col2:
    st.info(
        f"📍 **Highest Spending Location**\n\n"
        f"**{top_location}**"
    )

with col3:
    st.info(
        f"💳 **Most Used Payment Type**\n\n"
        f"**{top_payment}**"
    )


# TABS
overview_tab, transactions_tab, insights_tab = st.tabs(
    [
        "🏠 Overview",
        "💳 My Transactions",
        "📈 Spending Insights"
    ]
)


# OVERVIEW TAB
with overview_tab:

    st.markdown(
        '<div class="section-title">📈 Spending Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    # ---------- CATEGORY CHART ----------
    with col1:
        category_chart = (
            filtered_df.groupby("Category", as_index=False)["Amount"]
            .sum()
            .sort_values("Amount", ascending=False)
        )

        fig = px.bar(
            category_chart,
            x="Category",
            y="Amount",
            title="💰 Spending by Category",
            text_auto=".2s"
        )

        fig.update_layout(
            xaxis_title="Category",
            yaxis_title="Amount",
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ---------- PAYMENT CHART ----------
    with col2:
        payment_chart = (
            filtered_df.groupby("PaymentMethod", as_index=False)["Amount"]
            .sum()
        )

        fig = px.pie(
            payment_chart,
            names="PaymentMethod",
            values="Amount",
            hole=0.45,
            title="💳 Spending by Payment Method"
        )

        fig.update_layout(paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)

    # ---------- MONTHLY TREND ----------
    if "Month_Number" in filtered_df.columns:
        monthly = (
            filtered_df.dropna(subset=["Month_Number"])
            .groupby("Month_Number", as_index=False)["Amount"]
            .sum()
            .sort_values("Month_Number")
        )

        month_names = {
            1: "January", 2: "February", 3: "March",
            4: "April", 5: "May", 6: "June",
            7: "July", 8: "August", 9: "September",
            10: "October", 11: "November", 12: "December"
        }

        monthly["Month"] = monthly["Month_Number"].map(month_names)

        if not monthly.empty:
            fig = px.line(
                monthly,
                x="Month",
                y="Amount",
                markers=True,
                title="📅 How Your Spending Changes Over Time"
            )

            fig.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white"
            )

            st.plotly_chart(fig, use_container_width=True)

    # ---------- TIME OF DAY ----------
    time_chart = (
        filtered_df.groupby("TimeOfDay", as_index=False)["Amount"]
        .sum()
    )

    fig = px.bar(
        time_chart,
        x="TimeOfDay",
        y="Amount",
        title="🕒 Spending by Time of Day",
        text_auto=".2s"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig, use_container_width=True)


# TRANSACTIONS TAB
with transactions_tab:

    st.markdown(
        '<div class="section-title">💳 My Transactions</div>',
        unsafe_allow_html=True
    )

    st.caption("Search and review your transactions.")

    search_text = st.text_input(
        "🔎 Search transactions",
        placeholder="Search by description..."
    )

    transaction_view = filtered_df.copy()

    if search_text and "Description" in transaction_view.columns:
        transaction_view = transaction_view[
            transaction_view["Description"]
            .astype(str)
            .str.contains(search_text, case=False, na=False)
        ]

    st.write(
        f"**{len(transaction_view):,} transactions found**"
    )

    display_columns = [
        column for column in [
            "Date",
            "Description",
            "Amount",
            "Category",
            "PaymentMethod",
            "Location",
            "TransactionType",
            "MerchantType",
            "TimeOfDay"
        ]
        if column in transaction_view.columns
    ]

    st.dataframe(
        transaction_view[display_columns]
        .sort_values("Amount", ascending=False),
        use_container_width=True,
        height=500
    )

    csv_data = transaction_view.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download These Transactions",
        data=csv_data,
        file_name="my_filtered_transactions.csv",
        mime="text/csv"
    )


# SPENDING ISIGHTS TAB
with insights_tab:

    st.markdown(
        '<div class="section-title">📈 Understand Your Spending</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Simple insights based on the transactions you selected."
    )

    col1, col2 = st.columns(2)

    # TOP CATEGORY 
    with col1:
        category_data = (
            filtered_df.groupby("Category", as_index=False)["Amount"]
            .sum()
            .sort_values("Amount", ascending=False)
        )

        fig = px.bar(
            category_data,
            x="Amount",
            y="Category",
            orientation="h",
            title="💰 Where Is Your Money Going?",
            text_auto=".2s"
        )

        fig.update_layout(
            yaxis={"categoryorder": "total ascending"},
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(fig, use_container_width=True)

    # LOCATION 
    with col2:
        location_data = (
            filtered_df.groupby("Location", as_index=False)["Amount"]
            .sum()
            .sort_values("Amount", ascending=False)
        )

        fig = px.bar(
            location_data,
            x="Location",
            y="Amount",
            title="📍 Where Do You Spend the Most?",
            text_auto=".2s"
        )

        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(fig, use_container_width=True)

    #  PAYMENT VS CATEGORY 
    st.markdown(
        '<div class="section-title">💳 Category vs Payment Method</div>',
        unsafe_allow_html=True
    )

    pivot_data = pd.pivot_table(
        filtered_df,
        values="Amount",
        index="Category",
        columns="PaymentMethod",
        aggfunc="sum",
        fill_value=0
    )

    if not pivot_data.empty:
        fig = px.imshow(
            pivot_data,
            text_auto=".0f",
            aspect="auto",
            title="How You Pay for Different Categories"
        )

        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(fig, use_container_width=True)

    # SIMPLE TAKEAWAYS 
    st.markdown(
        '<div class="section-title">💡 Helpful Takeaways</div>',
        unsafe_allow_html=True
    )

    high_value_count = int(
        (filtered_df["Amount"] > 5000).sum()
    )

    if average_transaction <= 5000:
        message = (
            f"Your average transaction is ₹{average_transaction:,.0f}. "
            "Most transactions in this selection are within a lower spending range."
        )
    elif average_transaction <= 15000:
        message = (
            f"Your average transaction is ₹{average_transaction:,.0f}. "
            "Your selected transactions show a moderate spending range."
        )
    else:
        message = (
            f"Your average transaction is ₹{average_transaction:,.0f}. "
            "Your selection contains several higher-value transactions."
        )

    st.success(message)

    st.info(
        f"🔥 You have **{high_value_count:,}** transactions above ₹5,000 "
        "in the current selection."
    )

    st.info(
        f"💰 Your largest transaction in this selection is "
        f"**₹{highest_transaction:,.0f}**."
    )


# FOOTER
st.markdown("---")

st.markdown(
    """
    <div class="footer">
        <b>FinSight</b> • Personal Finance Dashboard
        <br>
        Track your spending • Explore your transactions •
        Understand your financial habits
    </div>
    """,
    unsafe_allow_html=True
)
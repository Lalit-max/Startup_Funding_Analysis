# ==========================
# 1. IMPORTS & CONFIGURATION
# ==========================
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(layout="wide",page_title="Start-up Analysis")

# ==========================
# 2. DATA LOADING
# ==========================

startup=pd.read_csv("startup_cleaned.csv")
startup["date"]=pd.to_datetime(startup["date"],errors="coerce")
startup.rename(columns={"amount":"amount_in_cr"},inplace=True)
startup["year"] = startup["date"].dt.year
startup["month"]= startup["date"].dt.month


# ==========================
# 3. HELPER FUNCTIONS
# ==========================

#=====
#investor analysis
#=====

#----------MOST RECENT INVESTMENTS---------
def load_investor_details(investor):
    st.title(investor)
    st.subheader("Most Recent Investments")

    #investors null data handling with case sensitivity 
    inv_df=startup[startup["investors"].fillna("").str.contains(investor,case=False)]

    if inv_df.empty:
        st.warning("No investment data available for this investor.")
        return
    
    #last 5 investments
    last_5=inv_df.sort_values("date",ascending=False)[["date","startup","vertical","city","round","amount_in_cr"]].head(5)

    #df show
    st.dataframe(last_5)

#------------BIGGEST INVESTMENTS---------------

    col1,col2=st.columns(2)
    with col1:
        #biggest investments
        big_invest=inv_df.groupby("startup")["amount_in_cr"].sum().sort_values(ascending=False).head()
        st.subheader("Biggest Investments")
    
        fig,ax=plt.subplots()
        ax.bar(big_invest.index,big_invest.values)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    with col2:
#-----------most invested sectors----------------------

        sector_invest=inv_df.groupby("vertical")["amount_in_cr"].sum()
        sector_invest = sector_invest[sector_invest > 0]  # remove zero-amounts
        st.subheader("Sectors invested in")

        if sector_invest.empty:
            st.info("No valid sector investment data available (all are zero).")
        else:
            fig1, ax1 = plt.subplots()
            ax1.pie(sector_invest, labels=sector_invest.index, autopct="%0.01f%%")
            st.pyplot(fig1)

    col3, col4 = st.columns(2)
#------------Most Invested rounds------------------------

    with col3:
        st.subheader("Most Invested Rounds")

        # Safely filter investor data
        round_invest = inv_df.groupby("round")["amount_in_cr"].sum()

        # Remove zero or NaN investments
        round_invest = round_invest[round_invest > 0]

        if round_invest.empty:
            st.info("No valid round investment data available (all are zero or missing).")
        else:
            fig3, ax3 = plt.subplots()
            ax3.pie(round_invest, labels=round_invest.index, autopct="%0.01f%%")
            st.pyplot(fig3)

    with col4:
#-----------investment cities---------------------

        st.subheader("Investment Cities")

        # Safely filter investor data
        city_invest = inv_df.groupby("city")["amount_in_cr"].sum()

        # Remove zero or NaN investments
        city_invest = city_invest[city_invest > 0]

        if city_invest.empty:
            st.info("No valid city investment data available (all are zero or missing).")
        else:
            fig4, ax4 = plt.subplots()
            ax4.pie(city_invest, labels=city_invest.index, autopct="%0.01f%%")
            st.pyplot(fig4)

#-----------------Year wise investments---------------

    YoY=startup[startup["investors"].str.contains(investor)].groupby("year")["amount_in_cr"].sum()
    st.subheader("YoY Investment")
    fig2,ax2=plt.subplots()
    ax2.plot(YoY.index,YoY.values)
    st.pyplot(fig2)

#======
#startup analysis
#======

def load_startup_details(startup_name):
    st.title(startup_name)

    df = startup[startup["startup"] == startup_name]

    if df.empty:
        st.warning("No data available for this startup.")
        return

    # -------- Startup Overview --------
    st.subheader("Startup Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Industry", df["vertical"].iloc[0])

    with col2:
        st.metric("Sub-Industry", df["subvertical"].iloc[0])

    with col3:
        st.metric("Location", df["city"].iloc[0])

    st.info("Founder information is not available in the source dataset.")

    # -------- Funding History --------
    st.subheader("Funding History")

    funding_table = df.sort_values("date")[[
        "date", "round", "investors", "amount_in_cr"
    ]]

    st.dataframe(funding_table)

    # -------- Funding Summary --------
    st.subheader("Funding Summary")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric("Total Funding (Cr)", round(df["amount_in_cr"].sum(), 2))

    with col5:
        st.metric("Funding Rounds", df.shape[0])

    with col6:
        st.metric("Latest Round", df.sort_values("date")["round"].iloc[-1])

    # -------- Similar Startups --------
    st.subheader("Similar Startups")

    similar = startup[
        (startup["vertical"] == df["vertical"].iloc[0]) &
        (startup["city"] == df["city"].iloc[0]) &
        (startup["startup"] != startup_name)
    ]["startup"].unique()[:5]

    if len(similar) == 0:
        st.info("No similar startups found based on industry and location.")
    else:
        for s in similar:
            st.write("•", s)


#======
#overall analysis
#======
def overall_analysis():
    st.title("Overall Start-up Funding Analysis")

    # ======================
    # KPI CARDS
    # ======================
    total_funding = startup["amount_in_cr"].sum()
    max_funding = startup["amount_in_cr"].max()
    avg_funding = startup["amount_in_cr"].mean()
    total_startups = startup["startup"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Funding (Cr)", round(total_funding, 2))
    col2.metric("Max Funding (Cr)", round(max_funding, 2))
    col3.metric("Avg Funding (Cr)", round(avg_funding, 2))
    col4.metric("Funded Startups", total_startups)

    st.divider()

    # ======================
    # MoM FUNDING TREND
    # ======================
    st.subheader("Month-on-Month Funding Trend")

    mom = startup.groupby(["year", "month"])["amount_in_cr"].sum().reset_index()
    mom["date"] = pd.to_datetime(
        mom["year"].astype(str) + "-" + mom["month"].astype(str)
    )

    fig, ax = plt.subplots()
    ax.plot(mom["date"], mom["amount_in_cr"])
    ax.set_xlabel("Month")
    ax.set_ylabel("Funding (Cr)")
    st.pyplot(fig)

    st.dataframe(mom.sort_values("date", ascending=False))

    st.divider()

    # ======================
    # SECTOR ANALYSIS
    # ======================
    st.subheader("Top Sectors by Funding")

    sector_funding = (
        startup.groupby("vertical")["amount_in_cr"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig1, ax1 = plt.subplots()
    ax1.pie(sector_funding, labels=sector_funding.index, autopct="%0.1f%%")
    st.pyplot(fig1)

    # ======================
    # FUNDING TYPE
    # ======================
    st.subheader("Funding Type Distribution")

    round_funding = startup.groupby("round")["amount_in_cr"].sum()
    round_funding = round_funding[round_funding > 0]

    fig2, ax2 = plt.subplots()
    ax2.pie(round_funding, labels=round_funding.index, autopct="%0.1f%%")
    st.pyplot(fig2)

    st.divider()

    # ======================
    # CITY-WISE FUNDING
    # ======================
    st.subheader("Top Cities by Funding")

    city_funding = (
        startup.groupby("city")["amount_in_cr"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig3, ax3 = plt.subplots()
    ax3.bar(city_funding.index, city_funding.values)
    plt.xticks(rotation=45)
    st.pyplot(fig3)

    st.divider()

    # ======================
    # TOP STARTUPS
    # ======================
    st.subheader("Top Funded Startups (Overall)")

    top_startups = (
        startup.groupby("startup")["amount_in_cr"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.dataframe(top_startups.reset_index())

    # ======================
    # TOP INVESTORS (STRING-BASED)
    # ======================
    st.subheader("Top Investors")

    investors_series = (
        startup["investors"]
        .str.split(", ")
        .explode()
    )

    top_investors = investors_series.value_counts().head(10)
    st.dataframe(top_investors.reset_index(name="Number of Investments"))

    st.divider()

    # ======================
    # FUNDING HEATMAP
    # ======================
    st.subheader("Funding Heatmap (Year vs Month)")

    heatmap_data = startup.pivot_table(
        values="amount_in_cr",
        index="year",
        columns="month",
        aggfunc="sum"
    )

    fig4, ax4 = plt.subplots()
    im = ax4.imshow(heatmap_data, aspect="auto")
    plt.colorbar(im)
    ax4.set_xlabel("Month")
    ax4.set_ylabel("Year")
    st.pyplot(fig4)



# ==========================
# 4. MAIN APP FLOW
# ==========================

st.sidebar.title("Start-up Funding Analysis")
option=st.sidebar.selectbox("Select One",["Overall Analysis","Startup Analysis","Investment Analysis"])

if option=="Overall Analysis":
    overall_analysis()

elif option == "Startup Analysis":
    option1 = st.sidebar.selectbox(
        "Select Startup",
        sorted(startup["startup"].unique())
    )
    btn1 = st.sidebar.button("Find Startup Details")

    if btn1:
        load_startup_details(option1)

else:
    option2=st.sidebar.selectbox("Select Investor",sorted(set(startup["investors"].str.split(",").sum())))
    btn2=st.sidebar.button("Find Investor Details")
    if btn2:
        load_investor_details(option2)

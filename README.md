🚀 Startup Funding Analysis Dashboard

An interactive Streamlit-based data analytics dashboard to analyze startup funding trends in India across investors, startups, sectors, cities, and time.

📌 Project Overview

  This project analyzes historical startup funding data to provide three levels of insights:
  
  Overall Analysis – Macro funding trends and ecosystem-level insights
  
  Startup Analysis – Deep dive into individual startup funding history
  
  Investor Analysis – Investment behavior and portfolio insights for investors
  
  The dashboard is designed with real-world analytics principles, focusing on data correctness, modular code structure, and clear visual storytelling.

🧠 Problem Statement

  Startup funding data is often available in raw tabular form, making it difficult to:
  
  Track funding trends over time
  
  Compare sectors, cities, and funding stages
  
  Analyze investor behavior and startup growth
  
  This project converts raw funding data into a structured, interactive decision-support dashboard.

📊 Dataset Description

  Source: Cleaned startup funding dataset (startup_cleaned.csv)
  
  Rows: 2,819 funding records
  
  Columns:
  
  Column	Description
  date	Funding date
  startup	Startup name
  vertical	Industry / sector
  subvertical	Sub-industry
  city	Startup location
  investors	Investors involved (comma-separated)
  round	Funding stage
  amount_in_cr	Funding amount (in Crores)
  
🛠️ Tech Stack

  Python
  
  Pandas – Data cleaning & transformation
  
  NumPy – Numerical operations
  
  Streamlit – Interactive dashboard UI
  
  Matplotlib – Data visualization
  
  Git & GitHub – Version control

🧩 Dashboard Features
1️⃣ Overall Analysis

  Provides a macro-level view of the startup ecosystem.
  
  KPI cards:
  
  Total funding
  
  Maximum funding
  
  Average funding
  
  Total funded startups
  
  Month-on-Month (MoM) funding trends (chart + table)
  
  Sector-wise funding analysis (top sectors)
  
  Funding type distribution (rounds)
  
  City-wise funding comparison
  
  Top startups (overall)
  
  Top investors (based on investment count)
  
  Year–Month funding heatmap for trend detection

2️⃣ Startup Analysis

  Detailed view of an individual startup.
  
  Startup overview:
  
  Industry
  
  Sub-industry
  
  Location
  
  Funding history:
  
  Date
  
  Funding stage
  
  Investors
  
  Amount
  
  Funding summary:
  
  Total funding
  
  Number of funding rounds
  
  Latest funding stage
  
  Similar startups:
  
  Identified using industry and city similarity
  
  Note: Founder information is not present in the source dataset and is intentionally not assumed.

3️⃣ Investor Analysis

  Insights into investor behavior and portfolio distribution.
  
  Most recent investments
  
  Biggest investments by startup
  
  Sector-wise investment distribution
  
  Funding round preferences
  
  City-wise investment distribution
  
  Year-on-Year (YoY) investment trends
  
  To ensure correct investor-level analysis, the project normalizes comma-separated investor data using string split and explode logic.

⚙️ Key Data Engineering Concepts Used

  Handling missing values safely (fillna)
  
  Date parsing and feature extraction (year, month)
  
  Data normalization using split() and explode()
  
  GroupBy aggregations for analytical insights
  
  Defensive programming for empty data scenarios
  
  Modular function-based Streamlit architecture

📁 Project Structure
├── startup_cleaned.csv
├── app.py
├── README.md
└── requirements.txt

▶️ How to Run the Project

  Clone the repository:
  
  git clone https://github.com/Lalit-max/Startup_Funding_Analysis.git
 
  
  Install dependencies:
  
  pip install -r requirements.txt
  
  
  Run the Streamlit app:
  
  streamlit run app.py

🚧 Limitations

  Founder and founding year information is not available in the dataset
  
  Investor analysis relies on text-based normalization
  
  Dataset is historical and static (no real-time updates)
  
  These limitations are clearly acknowledged to maintain data integrity.

🔮 Future Improvements

  Add external APIs for founder and company metadata
  
  Improve investor similarity analysis
  
  Add interactive filters and advanced charts
  
  Deploy dashboard on Streamlit Cloud
  
  Introduce ML-based funding trend forecasting

🎯 Learning Outcomes

  Built a production-style Streamlit dashboard
  
  Learned data normalization for many-to-many relationships
  
  Applied analytical thinking to derive insights from imperfect data
  
  Designed dashboards with interview-ready structure and clarity

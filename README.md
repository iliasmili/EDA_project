# 🏠 Housing Price Analysis — Exploratory Data Analysis (EDA)

## 📌 Project Overview
An exploratory data analysis (EDA) project using Python to analyze 
housing price data. The project examines patterns, distributions, 
correlations, and relationships between housing features and prices.

---

## 🛠️ Tools & Technologies
- **Python** (pandas, matplotlib, seaborn)
- **VSCode**

---

## 📂 Project Structure
```
housing_analysis/
│
├── Housing.csv                 ← Raw dataset
├── analysis.py                 ← Load & preview data (first 5 rows)
├── analysis10rows.py           ← Preview first 10 rows
├── analysisdatashape.py        ← Dataset dimensions (rows & columns)
├── analysisdescribe.py         ← Statistical summary
├── analysisinfo.py             ← Data types & missing values
├── analysislastrows.py         ← Preview last rows
├── ranges.py                   ← Price range (max - min)
├── destributions.py            ← Price distribution histogram
├── visualization.py            ← Area vs Price scatter plot
├── correlationheatmap.py       ← Feature correlation heatmap
└── README.md
```

---

## 🔄 Project Steps

### 1️⃣ Data Exploration
- Previewed first and last rows of the dataset
- Checked dataset shape (rows & columns)
- Reviewed data types and missing values
- Generated statistical summary (mean, min, max, std)

### 2️⃣ Analysis
- Calculated price range across all properties
- Identified key statistical patterns in the data

### 3️⃣ Visualizations
- **Histogram** → Price distribution across all properties
- **Scatter Plot** → Relationship between area and price
- **Correlation Heatmap** → Relationships between all numeric features

---

## 📊 Key Findings

- 📈 **Area and price** show a positive correlation — 
  larger properties tend to cost more
- 🔥 **Correlation heatmap** reveals which features 
  most strongly influence price
- 📊 **Price distribution** shows the spread and 
  concentration of property prices

---

## 📁 Dataset
- **File:** Housing.csv
- **Domain:** Real Estate
- **Target Variable:** Price

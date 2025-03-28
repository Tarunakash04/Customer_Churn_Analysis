# Telecom Customer Churn Analysis  

## Overview  
Customer churn is a major challenge in the telecom industry, impacting revenue and customer retention.  
This project utilizes **PySpark** to analyze customer data, identify key churn factors,  
and build predictive models to improve retention strategies.  

## Tech Stack  
- **Programming Language**: Python  
- **Big Data Framework**: Apache Spark (PySpark)  
- **Machine Learning**: Spark MLlib  
- **Visualization**: Matplotlib, Seaborn  
- **Data Processing**: Spark DataFrames  

## Dataset Overview  
The dataset contains telecom customer details, service usage, and churn status.  

- 📌 **CustomerID** - Unique customer identifier  
- 📌 **Tenure** - Number of months a customer has stayed  
- 📌 **MonthlyCharges** - Monthly bill amount  
- 📌 **TotalCharges** - Total amount paid by the customer  
- 📌 **Contract** - Type of contract (Month-to-Month, One Year, Two Years)  
- 📌 **Churn** - Whether the customer left (**Yes/No**)  

## 🔍 Exploratory Data Analysis (EDA)  
✅ **Performed data cleaning** and handled missing values using **PySpark DataFrames**  
✅ **Identified feature correlations** using **groupBy() and aggregations**  
✅ **Visualized churn distribution** using **Seaborn and Matplotlib**  

## 🤖 Machine Learning Approach  

### 1️⃣ Feature Engineering  
✔️ Converted categorical variables using **StringIndexer**  
✔️ Scaled numerical features using **MinMaxScaler**  

### 2️⃣ Model Selection (PySpark MLlib)  
🚀 **Logistic Regression**  
🚀 **Random Forest Classifier**  
🚀 **Gradient Boosted Trees (GBTClassifier)**  

### 3️⃣ Evaluation Metrics  
📌 **Accuracy**  
📌 **Precision & Recall**  
📌 **F1-score**  
📌 Evaluated models using **BinaryClassificationEvaluator**  

## 📌 Key Findings  
✅ Customers with **month-to-month contracts** have the highest churn rate  
✅ **Higher monthly charges** increase churn probability  
✅ Customers with **longer tenure** are less likely to churn  

## 📜 License  
This project is licensed under the **MIT License**.  

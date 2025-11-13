# End-to-End Healthcare Claims & Fraud Analysis

![Healthcare Dashboard Screenshot](dashboards/dashboard_screenshot.png)
---

### 1. Project Overview

This project is an end-to-end data analysis of a synthetic healthcare claims dataset. The primary goal is to clean and prepare the data, perform exploratory data analysis (EDA) to find insights, and build an interactive Power BI dashboard to present key metrics, cost drivers, and potential fraud indicators.

This repository demonstrates a complete data analysis workflow:
* **Data Cleaning:** Using Python (Pandas) to clean and transform raw data.
* **Database Management:** Setting up a SQLite database to store and query the cleaned data.
* **Exploratory Data Analysis (EDA):** Using Python (Matplotlib/Seaborn) and SQL to uncover patterns.
* **Data Visualization:** Building a dynamic dashboard in Power BI for stakeholder presentation.

---

### 2. Tools & Technologies

* **Python 3.13**
    * **Pandas & NumPy:** For data cleaning, manipulation, and feature engineering.
    * **Matplotlib & Seaborn:** For static data visualization in the EDA phase.
    * **SQLite3:** For database creation and data storage.
* **SQL:** For querying and aggregating data from the database.
* **Power BI Desktop:** For creating the final interactive dashboard.

---

### 3. Project Workflow

The project is broken down into four main stages, with a corresponding script for each:

**1. Data Cleaning (`scripts/01_data_cleaning.py`)**
* Loaded the raw `healthcare_dataset.csv`.
* Standardized column names (lowercase, stripped spaces, replaced ' ' with '_').
* Converted `date_of_admission` and `discharge_date` to datetime objects.
* Filtered out invalid data (e.g., `billing_amount` <= 0).
* **Feature Engineering:**
    * Created `length_of_stay` by subtracting `date_of_admission` from `discharge_date`.
    * Created a `fraud_flag` (as a `0` or `1`) to identify high-risk claims, defined as those with a `billing_amount > 40000` AND a `length_of_stay > 10`.
* Exported the cleaned data to `data/healthcare_cleaned.csv`.

**2. Database Setup (`scripts/03_database_setup.py`)**
* Loaded the `healthcare_cleaned.csv` file into a Pandas DataFrame.
* Established a connection to a new SQLite database (`data/healthcare.db`).
* Wrote the entire cleaned DataFrame to a SQL table named `claims`.
* Performed an example query (`AVG(billing_amount)` by `medical_condition`) to verify the database was working.

**3. Exploratory Data Analysis (`notebooks/EDA_Visualization.ipynb`)**
* This Jupyter Notebook combines insights from `EDA_Visualization.py` and `sql_queries.py`.
* **KPI Calculation:** Calculated foundational metrics like Total Claims, Total & Average Billing, Avg. Length of Stay, and Fraud Rate (%).
* **Univariate Analysis:** Plotted distributions for key columns:
    * `billing_amount` (Histogram)
    * `admission_type` (Bar Chart)
* **Bivariate Analysis:** Investigated relationships to find insights:
    * `Average Billing by Medical Condition` (Bar Chart)
    * `Billing Amount vs. Length of Stay`, highlighting the `fraud_flag` (Scatter Plot)

**4. Dashboarding (`dashboards/Doctor_Billing_sum_visualisation.pbix`)**
* Connected Power BI Desktop to the `healthcare_cleaned.csv` data.
* Created DAX measures to aggregate the key metrics identified in the EDA.
* Designed an interactive dashboard featuring:
    * A KPI card banner for at-a-glance metrics (Total Billing, Fraud Rate, Total Patients, Avg. Length of Stay).
    * Charts to visualize cost drivers (e.g., Billing by Medical Condition, Billing by Admission Type).
    * A detailed matrix showing hospital and doctor performance.
    * Slicers for `Hospital`, `Doctor_Name`, and `Insurance_Provider` to allow for dynamic filtering.

---

### 4. Key Insights & Findings

* **Cost Drivers:** The EDA clearly showed that **Medical Condition** and **Admission Type** are the primary drivers of cost. Conditions like Cancer and Heart Disease had significantly higher average billing amounts.
* **Fraud Indication:** The engineered `fraud_flag` successfully isolated a high-risk cohort of claims (high bill, long stay). The scatter plot showed a clear visual cluster for these claims, which were then analyzed by doctor and hospital.
* **Actionable Insights:** The dashboard allows administrators to quickly identify specific doctors, hospitals, or insurance providers with unusually high billing amounts or a high incidence of flagged claims, enabling targeted audits.

---

### 5. Repository Structure

Healthcare_Claims_Analysis/ │ ├─ data/ │ ├─ healthcare_dataset.csv (Raw data, not included) │ ├─ healthcare_cleaned.csv (Output of 01_data_cleaning.py) │ └─ healthcare.db (Output of 03_database_setup.py) │ ├─ scripts/ │ ├─ 01_data_cleaning.py (Cleans and prepares data) │ ├─ 02_EDA.py (Original script for EDA visuals) │ ├─ 03_database_setup.py (Creates the SQLite database) │ └─ 04_sql_queries.py (Original script for KPI calculations) │ ├─ notebooks/ │ └─ EDA_Visualization.ipynb (Full EDA and analysis) │ ├─ dashboards/ │ ├─ Doctor_Billing_sum_visualisation.pbix (The Power BI file) │ └─ dashboard_screenshot.png (Screenshot of the dashboard) │ └─ README.md


### 6. How to Run This Project

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/Healthcare_Claims_Analysis.git](https://github.com/your-username/Healthcare_Claims_Analysis.git)
    cd Healthcare_Claims_Analysis
    ```
2.  **Install Dependencies:**
    ```bash
    pip install pandas numpy matplotlib seaborn jupyter notebook
    ```
3.  **Run the Python Scripts (in order):**
    ```bash
    python scripts/01_data_cleaning.py
    python scripts/03_database_setup.py
    ```
4.  **Explore the EDA:**
    ```bash
    python -m notebook notebooks/EDA_Visualization.ipynb
    ```
    (This will open the notebook in your browser.)
5.  **View the Dashboard:**
    * Open the `dashboards/Doctor_Billing_sum_visualisation.pbix` file using **Power BI Desktop**.

### 5. Repository Structure
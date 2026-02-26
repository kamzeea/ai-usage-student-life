# AI Usage in Student Life — Data Analysis & Interactive Dashboard

## Project Overview

This project analyzes how students use **AI assistants** and identifies which factors influence the **success** of an AI usage session. Using a dataset of **10,000 simulated student AI sessions**, we applied data science techniques, statistical testing, and interactive visualization to uncover behavioral patterns and insights.

The project concludes with a deployed **Streamlit web application** that allows users to explore findings through **interactive charts and dashboards**.

---

## Project Objective

The goal of this project was to determine:

- Which factors influence **successful AI sessions** among students  
- How **session characteristics** impact satisfaction  
- Whether **session length** varies across disciplines or task types  
- How AI outcomes affect **willingness to reuse** AI tools  

---

## Dataset

**Dataset:** AI Assistant Usage in Student Life (Synthetic Dataset)  
Each record represents an AI usage session and includes:

- **Student Level**  
- **Academic Discipline**  
- **Session Length (minutes)**  
- **Total Prompts Used**  
- **Task Type**  
- **AI Assistance Rating (1–5)**  
- **Satisfaction Rating (1–5)**  
- **Session Outcome**  
- **Would Use AI Again** (Boolean)  

**Total Records:** 10,000 sessions  

**Dataset Source:**  
[AI Assistant Usage in Student Life — Synthetic Dataset](https://www.kaggle.com/datasets/ayeshasal89/ai-assistant-usage-in-student-life-synthetic)

---

## Skills Demonstrated

**Data Analysis**

- Exploratory Data Analysis (**EDA**)  
- Descriptive statistics  
- Correlation analysis  
- Feature comparison using **groupby** operations  

**Statistical Methods**

- Correlation testing  
- **ANOVA** hypothesis testing  
- Mean comparison across groups  

**Data Engineering**

- Data cleaning with **pandas**  
- Handling **null** and **duplicate** values  
- Encoding categorical variables  

**Visualization**

- Histograms  
- Bar charts  
- Pie charts  
- Distribution analysis  

**Application Development**

- **Streamlit** dashboard development  
- Multi-page web application design  
- Migrating from **Jupyter Notebook → production**  

---

## Technologies Used

- **Python**  
- **pandas**  
- **matplotlib**  
- **seaborn**  
- **Streamlit**  
- **Jupyter Notebook**  
- **GitHub**  
- **Anaconda**  

---

## Project Workflow

### Data Cleaning

- Checked for null values using `isnull().sum()`  
- Verified unique session IDs  
- Removed potential duplicates  
- Encoded Boolean variables for analysis  

### Exploratory Data Analysis

Generated descriptive statistics including:

- Mean **session length**  
- **Satisfaction** distribution  
- **Prompt usage** trends  
- General **student behavior** patterns  

Used:

- `df.info()`  
- `df.describe()`  

### Statistical Analysis

**Correlation Analysis**

- Tested relationship between **session length** and **satisfaction**  
- Result: **Correlation ≈ -0.01**  
- ➡ Indicates no meaningful linear relationship between session duration and satisfaction.  

**ANOVA Testing**

| Comparison                      | Result            | p-value |
|---------------------------------|-------------------|--------:|
| Session Length by **Discipline** | Not significant   | 0.96    |
| Session Length by **Task Type**  | Significant       | 0.02    |

**Task type** influences session duration more than discipline.

### Visualizations Created

- **Session Length Distribution** (Histogram)  
- **Satisfaction Rating Distribution**  
- **Outcome vs Reuse Probability** (Bar Chart)  
- **Student Level vs Satisfaction**  
- **Discipline Prompt Usage** (Pie Chart)  

These visualizations helped communicate insights clearly and intuitively.

### Streamlit Dashboard

Developed an interactive **multi-page Streamlit web application** to present results.

**Features:**

- Interactive charts and filters  
- Multi-page navigation  
- Data insights dashboard  
- Public deployment via **Streamlit Community Cloud**  

**Key learning outcomes:**

- Converting notebooks into **production-ready apps**  
- Managing `requirements.txt`  
- Structuring multi-page **Streamlit** projects  
- Using **GitHub** for deployment workflow  

---

## Key Findings

- Session length does **not** strongly correlate with satisfaction.  
- **Task type** significantly impacts session duration.  
- **Successful outcomes** increase the likelihood of AI reuse.  
- Satisfaction ratings vary widely across sessions.  
- **Student level** shows minimal impact on satisfaction.  

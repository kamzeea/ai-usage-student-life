import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


st.set_page_config(page_title="Dataset Analysis Dashboard") #page title

sns.set(style="whitegrid", context="talk") #seaborn - visual appearance of plots

#store dataset in cache, to prevent rerunning func
@st.cache_data
def load_data():
    df = pd.read_csv('updated_cleaned_dataset1.csv') #cleaned dataset
    df1 = pd.read_csv('ai_assistant_usage_student_life.csv') #uncleaned dataset
    return df, df1

#calling function
df, df1 = load_data()

st.title("Dataset Overview")
st.subheader("Uncleaned Dataset")
    
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
	st.metric("Total Records", len(df1))
with col2:
	if 'Discipline' in df.columns:
		st.metric("Disciplines", df1['Discipline'].nunique())
with col3:
    if 'TotalPrompts' in df.columns:
        st.metric("Avg Prompts", f"{df1['TotalPrompts'].mean():.2f}")
with col4:
    if 'SatisfactionRating' in df.columns:
        st.metric("Avg Satisfaction", f"{df1['SatisfactionRating'].mean():.2f}")
with col5:
    if 'TaskType' in df.columns:
        st.metric("TaskType", f"{df1['TaskType'].nunique()}")
with col6:
    if 'StudentLevel' in df.columns:
        st.metric("StudentLevel", f"{df1['StudentLevel'].nunique()}")  # Fixed typo
with col7:
    if 'FinalOutcome' in df.columns:
        st.metric('FinalOutcome', f"{df1['FinalOutcome'].nunique()}")
    
st.markdown("---")
    
st.subheader("Dataset Preview")
st.dataframe(df1.head(10))
    
st.markdown("---")
    
st.subheader("Column Information")
col_info = pd.DataFrame({
    'Column': df1.columns, #outputs colums in df
    'Type': df1.dtypes.values, #values accepted
    'Non-Null': df1.count().values, #count null values
    'Null Count': df1.isnull().sum().values
    })
st.dataframe(col_info) #display df created
    
st.markdown("---")
    
st.subheader("Quick Statistics")
st.dataframe(df1.describe().head(4))




#cleaned dataset
st.title("Cleaned Dataset")
    
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    
with col1:
    st.metric("Total Records", len(df)) #displays metric as kpis 
with col2:
    if 'Discipline' in df.columns:
        st.metric("Disciplines", df['Discipline'].nunique())
with col3:
    if 'TotalPrompts' in df.columns:
        st.metric("Avg Prompts", f"{df['TotalPrompts'].mean():.2f}")
with col4:
    if 'SatisfactionRating' in df.columns:
        st.metric("Avg Satisfaction", f"{df['SatisfactionRating'].mean():.2f}")
with col5:
    if 'TaskType' in df.columns:
        st.metric("TaskType", f"{df['TaskType'].nunique()}")
with col6:
    if 'StudentLevel' in df.columns:
        st.metric("StudentLevel", f"{df['StudentLevel'].nunique()}")  # Fixed typo
with col7:
    if 'FinalOutcome' in df.columns:
        st.metric('FinalOutcome', f"{df['FinalOutcome'].nunique()}")
    
st.markdown("---")
    
st.subheader("Dataset Preview")
st.dataframe(df.head(15), use_container_width=True) #use_container_width- expands to fill the full width of container
    
st.markdown("---")
    
st.subheader("Column Information")
col_info = pd.DataFrame({ #creating and assigning a df
    'Column': df.columns,
    'Type': df.dtypes.values,
    'Non-Null': df.count().values,
    'Null Count': df.isnull().sum().values
    })
st.dataframe(col_info, use_container_width=True) #display dataframe
    
st.markdown("---")
    
st.subheader("Quick Statistics")
st.dataframe(df.describe().head(4))

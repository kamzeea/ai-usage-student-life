import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set style for visualizations
sns.set(style="whitegrid")

# Load the cleaned dataset
df = pd.read_csv('updated_cleaned_dataset1.csv')

# Compute correlations
correlation = df['SessionLengthMin'].corr(df['SatisfactionRating'])
print(f"Correlation between SessionLengthMin and SatisfactionRating: {correlation:.2f}")

# Analyze means by TaskType and StudentLevel
mean_by_task = df.groupby('TaskType').mean(numeric_only=True)[['SatisfactionRating', 'TotalPrompts']]
mean_by_student_level = df.groupby('StudentLevel').mean(numeric_only=True)[['SessionLengthMin', 'SatisfactionRating']]
print("\nMean SatisfactionRating and TotalPrompts by TaskType:")
print(mean_by_task)
print("\nMean SessionLengthMin and SatisfactionRating by StudentLevel:")
print(mean_by_student_level)

# Pie chart: Distribution of students by StudentLevel
plt.figure(figsize=(8, 6))
student_level_counts = df['StudentLevel'].value_counts()
plt.pie(student_level_counts, labels=student_level_counts.index, 
        autopct='%1.1f%%', 
        colors=["#3498db", "#e74c3c", "#2ecc71"], 
        startangle=90, textprops={'fontsize': 11})
plt.title('Distribution of Students by Level')
plt.tight_layout()
plt.savefig('student_level_pie.png')
plt.show()

# Bar chart: Mean SatisfactionRating by TaskType
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='TaskType', y='SatisfactionRating', errorbar=None, color='#3498db')
plt.title('Mean Satisfaction Rating by Task Type')
plt.xlabel('Task Type')
plt.ylabel('Mean Satisfaction Rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('satisfaction_by_tasktype.png')
plt.show()

# Bar chart: Mean Total Prompts by TaskType
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='TaskType', y='TotalPrompts', errorbar=None, color='#e74c3c')
plt.title('Mean Total Prompts by Task Type')
plt.xlabel('Task Type')
plt.ylabel('Mean Total Prompts')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('prompts_by_tasktype.png')
plt.show()

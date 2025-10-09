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
mean_by_task = df.groupby('TaskType').mean(numeric_only=True)[['SessionLengthMin', 'SatisfactionRating']]
mean_by_student_level = df.groupby('StudentLevel').mean(numeric_only=True)[['SessionLengthMin', 'SatisfactionRating']]
print("\nMean SessionLengthMin and SatisfactionRating by TaskType:")
print(mean_by_task)
print("\nMean SessionLengthMin and SatisfactionRating by StudentLevel:")
print(mean_by_student_level)

# Scatter plot: SessionLengthMin vs. SatisfactionRating, colored by TaskType, sized by StudentLevel
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='SessionLengthMin', y='SatisfactionRating', hue='TaskType', size='StudentLevel', sizes=(50, 200))
plt.title('Session Length vs. Satisfaction Rating by Task Type and Student Level')
plt.xlabel('Session Length (Minutes)')
plt.ylabel('Satisfaction Rating')
plt.savefig('scatter_plot.png')
plt.show()

# Bar chart: Mean SatisfactionRating by TaskType
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='TaskType', y='SatisfactionRating', errorbar=None)
plt.title('Mean Satisfaction Rating by Task Type')
plt.xlabel('Task Type')
plt.ylabel('Mean Satisfaction Rating')
plt.savefig('bar_chart.png')
plt.show()


# Bar chart: Mean Total Prompts by TaskType
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='TaskType', y='TotalPrompts', errorbar=None)
plt.title('Mean Prompts by Task Type')
plt.xlabel('Total Prompts')
plt.ylabel('Mean Satisfaction Rating')
plt.savefig('bar_chart.png')
plt.show()

# Box plot: SessionLengthMin by StudentLevel
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='StudentLevel', y='SessionLengthMin', order=['High School', 'Undergraduate', 'Graduate'])
plt.title('Session Length Distribution by Student Level')
plt.xlabel('Student Level')
plt.ylabel('Session Length (Minutes)')
plt.savefig('box_plot.png')
plt.show()

"""# Option 3: Histogram with overlapping distributions
plt.figure(figsize=(12, 6))
for level, color in zip(['High School', 'Undergraduate', 'Graduate'], 
                        ['#3498db', '#e74c3c', '#2ecc71']):
    data = df[df['StudentLevel'] == level]['SessionLengthMin']
    plt.hist(data, bins=20, alpha=1.6, label=level, color=color, edgecolor='black')

plt.title('Session Length Distribution Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Session Length (Minutes)', fontsize=12)
plt.ylabel('Number of Sessions', fontsize=12)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('histogram_comparison.png')
plt.show()"""

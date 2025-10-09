import pandas as pd
from scipy import stats

df = pd.read_csv('updated_cleaned_dataset1.csv')

groups = [group['SessionLengthMin'].values for name, group in df.groupby('Discipline')]

f_stat, p_value = stats.f_oneway(*groups)

print(f'F-statistic: {f_stat:.2f}')
print(f'P-value: {p_value:.2f}')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace with your dataset path)
file_path = r'C:\Users\RUSHU\Desktop\Book1.xlsx'
data = pd.read_excel(file_path)

# Selecting relevant numerical columns for analysis
numerical_cols = ['PEOPLE_POSITIVE_CASES_COUNT', 'PEOPLE_DEATH_NEW_COUNT', 'PEOPLE_POSITIVE_NEW_CASES_COUNT', 'PEOPLE_DEATH_COUNT']

# Boxplot for the numerical columns
plt.figure(figsize=(10, 6))
sns.boxplot(data=data[numerical_cols])
plt.title('Box Plot for Numerical Columns')
plt.xticks(rotation=45)
plt.show()

# Scatter plot between PEOPLE_POSITIVE_NEW_CASES_COUNT and PEOPLE_DEATH_NEW_COUNT
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PEOPLE_POSITIVE_NEW_CASES_COUNT', y='PEOPLE_DEATH_NEW_COUNT', data=data)
plt.title('Scatter Plot: New Positive Cases vs New Deaths')
plt.show()

# Pearson Correlation Matrix for the numerical data
plt.figure(figsize=(8, 6))
correlation_matrix = data[numerical_cols].corr(method='pearson')
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Pearson Correlation Matrix')
plt.show()


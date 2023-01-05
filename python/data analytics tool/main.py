import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data.csv')

# Calculate summary statistics
mean = df['column1'].mean()
median = df['column1'].median()

# Generate a scatter plot
plt.scatter(df['column1'], df['column2'])
plt.title('Column 1 vs Column 2')
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.show()

# Print the summary statistics
print(f'Mean: {mean}')
print(f'Median: {median}')

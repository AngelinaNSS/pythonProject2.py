import pandas as pd

# Load the dataset
df = pd.read_csv('diabetes_clean.csv')

# Print the number of records in the dataset
num_records = df.shape[0]
print(f'The dataset contains {num_records} records.')

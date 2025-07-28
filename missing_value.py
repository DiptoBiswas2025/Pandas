import pandas as pd

# Step 1: Create a CSV
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Age': [15, 16, 17, None, 15, 16, 15],
    'Gender': ['Female', 'Male', None, 'Male', 'Female', 'Male', 'Female'],
    'Math': [85, 78, 92, 88, None, 75, 90],
    'English': [88, None, 79, 90, 84, None, 92],
    'Science': [90, 85, None, 87, 83, 80, None]
}

data_frame = pd.DataFrame(data)
data_frame.to_csv('data.csv', index=False)

# Step 2: Load the CSV
df = pd.read_csv('data.csv')

# print(df)

# Step 3: Detect Missing Data
print(df.isnull().sum())

# Step 4: Fill with Mean (only numeric columns)
df_mean = df.copy()
numeric_cols = df_mean.select_dtypes(include='number').columns
df_mean[numeric_cols] = df_mean[numeric_cols].fillna(df_mean[numeric_cols].mean())
print(df_mean)

# Step 5: Conditional fill (e.g., fill 'Gender' with 'Unknown')
df_conditional = df.copy()
df_conditional['Gender'] = df_conditional['Gender'].fillna('Unknown')
print("\nFill missing Gender with 'Unknown':")
print(df_conditional)
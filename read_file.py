import pandas as pd  # Import the pandas library

# To install package
# pip install (name of the library)
# py -m pip install (name of the library)

# Read the CSV file into a DataFrame
# 'data.csv' is the name of your CSV file. 
# Make sure it’s in the same directory or provide full path
df = pd.read_csv('data.csv')

# Display the first 5 rows of the DataFrame to check the data
print(df.head())
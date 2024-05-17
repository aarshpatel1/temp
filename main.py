import pandas

dictionary = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

# dataframe.loc[]

# Create a DataFrame
dataframe_1 = pandas.DataFrame(dictionary, index=['X', 'Y', 'Z'])
print(dataframe_1)

# Select a subset of rows and columns using label-based indexing
subset_1 = dataframe_1.loc[['X', 'Y'], ['A', 'B']]
print(subset_1)

# Select a single value using label-based indexing
value_1 = dataframe_1.loc['X', 'A']
print(f"Value at (X, A): {value_1}\n")

# dataframe.iloc[]

# Create a DataFrame
dataframe_2 = pandas.DataFrame(dictionary)
print(dataframe_2)

# Select a subset of rows and columns using integer-based indexing
subset_2 = dataframe_2.iloc[0:2, 0:2]
print(subset_2)

# Select a single value using integer-based indexing
value_2 = dataframe_2.iloc[0, 0]
print(f"Value at (0, 0): {value_2}")

# read csv
student_data = pandas.read_csv("student_data.csv")

x = student_data.iloc[0:2]
print(x)

y = student_data.loc[2, "area"]
print(y)

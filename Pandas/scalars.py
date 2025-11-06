import pandas as pd

# Create a Pandas Series with a scalar value
s = pd.Series([10]) 

# Extract the scalar value
scalar_value = s.iloc[0] 

# Convert the scalar value to a float
float_value = float(scalar_value) 

print(f"Original Pandas scalar: {scalar_value}, Type: {type(scalar_value)}")
print(f"Converted float: {float_value}, Type: {type(float_value)}")

# Example with a DataFrame
df = pd.DataFrame({'col1': [10.5], 'col2': ['abc']})
df_scalar = df.loc[0, 'col1']
df_float: float = df_scalar
print(f"\nOriginal DataFrame scalar: {df_scalar}, Type: {type(df_scalar)}")
print(f"Converted DataFrame float: {df_float}, Type: {type(df_float)}")
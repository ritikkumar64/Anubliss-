import pandas as pd

# Example: Create a DataFrame
data = {
    'Product': ['Chair', 'Table', 'Lamp', 'Sofa'],
    'Price': [50, 120, 30, 300],
    'Sales': [150, 200, 120, 80]
}

df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv('product_data.csv', index=False)

print("Data exported to 'product_data.csv'")
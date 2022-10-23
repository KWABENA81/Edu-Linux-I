import pandas as pd

technologies = ({
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", "Hadoop", "Spark", "Python"],
    'Fee': [22000, 25000, 23000, 24000, 26000, 25000, 25000, 22000],
    'Duration': ['30days', '50days', '55days', '40days', '60days', '35days', '55days', '50days'],
    'Discount': [1000, 2300, 1000, 1200, 2500, 1300, 1400, 1600]
})
df = pd.DataFrame(technologies, columns=['Courses', 'Fee', 'Duration', 'Discount'])
print(df)

# Use GroupBy() to compute the sum
df2 = df.groupby('Courses')['Fee'].sum()
print(df2)

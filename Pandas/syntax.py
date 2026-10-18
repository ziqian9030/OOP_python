import pandas as pd

df = pd.DataFrame({
    "name": ["Dara","Sophia","Vichea","Lina"],
    "age": [20,22,21,23],
    "City": ["Phonm Penh","Siem Reap","Phnom Penh","Battambang"],
    "Score": [82,92,78,95], 
})

s=pd.Series([10,20,30])
print(s)

s2=pd.Series([10,20,30], index=["a","b","c"])
print(s2["a"])

#show all data
print(df)  

#show how many rows and columns
print(df.shape)

# show all tpyes of data
print(df.dtypes)

# show first 2 rows
print(df.head(2))

# show last 2 rows
print(df.tail(2))

# show columns name
print(df.columns)
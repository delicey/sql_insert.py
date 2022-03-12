import pandas as pd

df = pd.read_csv("gods_unchained.csv")

print(df)

df["Quantity"] = 125,1200
print(df)

df.to_csv("modified.csv",index=False)

#df=df.to_excel("modified.xlsx")
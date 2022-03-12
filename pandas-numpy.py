#import numpy as np
import pandas as pd

df = pd.read_csv("pokemon_data.csv")

#print(df)

print(df.head(3))

print(df.tail(3))

print(df.iloc[2,1])

for index,row in df.iterrows():
    print(index,row["Name"])


print(df.loc[df["Type 1"] == "Fire"])

new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")]



#new_df = new_df.reset_index(drop=True) # alttakiyle aynı
#new_df.reset_index(drop=True, inplace=True)
print(new_df)

#new_df.to_csv ("filtered.csv")
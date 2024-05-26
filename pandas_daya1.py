import pandas as pd

a = [1,2,3,4]
my_arr = pd.Series(a, index=['a','b','c','d'])
my_arr2 = {"day1":452,"day2":365,"day3":236}
my_sries = pd.Series(my_arr2, index=["day1","day2"])
print(my_sries)
data = {
    "soccer point": [54,97,90],
    "math point": [80,56,12]
}
df = pd.DataFrame(data, index=['day3','day4','day5'])
print(df.loc['day5'])
df2 = pd.read_csv("bangalo.csv")
new_df = df2.dropna()
print(new_df.shape)
print(df2.shape)
#df = pd.read_json("data.json")
#print(df.to_string())
print(df2.head(10))
print(df2.tail(10))
print(df2.info())
#print(df2.shape)
#print(my_arr)
#print(my_arr2)
#print(my_arr['a'])
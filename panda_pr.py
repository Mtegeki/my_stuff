import pandas as pd
import csv


#jina = df["jina"]
apd_data = ["Alex",45,"Uganda", "Mwanaume"]
csv_path = "data.csv"
with open(csv_path, mode="a", newline="") as file:
    write = csv.writer(file)
    write.writerow(apd_data)
print("data appended successfuly")
df = pd.read_csv("data.csv")
df = df.drop_duplicates(subset=["Jina"], keep="first")
print(df[df["Jina"] == "Anord"])
#print(df)
df.to_csv(csv_path, index=False)

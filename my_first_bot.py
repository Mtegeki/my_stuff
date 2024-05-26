#project number 5
import pandas as pd
import csv

csv_path = "Knowlage.csv"
df = pd.read_csv(csv_path)

while True:
    user_input1 = input("Bot: Je, ungependa kufahamu kuhusu nini? : ")

    check_up = ""
    df_list = df["Mada"].tolist()


    if user_input1 in df_list:
        check_up = df.loc[df["Mada"] == user_input1,"Maana"].values[0]
        print(f"{user_input1 } ni {check_up}")
    else:
        user_leass = input(f"Bot: Tafadhali nipe maana ya neno {user_input1}: ")
        print("Bot: Asante kwa kunipa taarifa hizi!")
        user_kn = {"Mada":user_input1, "Maana":user_leass}
        df = df._append(user_kn, ignore_index=True)
        df.to_csv(csv_path, index=False)




'''user_kn = {"Mada":user_input1, "Maana":user_leass}
df = df.append(user_kn, ignore_index=True)
df.to_csv(csv_path, index=False)'''
'''with open(csv_path, mode="a", newline="") as file:
    write = csv.writer(file)
    write.writerow(user_kn)'''

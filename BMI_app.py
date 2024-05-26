#BMI app for everyone # project number 2
def bmi_finder(height, weight):
    cm_value = height / 100
    bmi = weight / (cm_value * cm_value )
    return bmi
user_h = input("please enter your height in centimeters: ")
user_w = input("please enter your weight in kilograms: ")
try:
    user_h = int(user_h)
    user_w = int(user_w)
except TypeError:
    user_h = int(user_h)
    user_w = int(user_w)
    
out_v = bmi_finder(user_h, user_w)

under = 18.5
balanced = 24.9
over_w = 29.9

def find_b():
    if out_v <= under:
        print("your under weight 🤷🤷")
        return 
    if out_v  <= balanced:
        print(" your health is balanced 😜")
        return 
    if out_v <= over_w:
        print("you health is overweight 🤗🤗 ")
    if out_v > over_w:
        print("ohhh no you have to exercise coz you have obesity ⏫😁")

find_b()
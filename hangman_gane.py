#project number 8
import random
import time

print(" \n hello karibu ucheze hangman  kutoka Nodegames \n")
time.sleep(1)
name  = input("Weka jina lako hapa \n : ")
print(f"karibu ndugu {name} jiandae kucheza game \n")
time.sleep(2)
print(f"hey {name} game inaenda kuanza sasa:")
time.sleep(3)

# exc_game
def main():
    global display
    global word
    global count
    global zilizo_chaguliwa
    global display_l
    orodha_chaguo = ["Nakupenda","chuo","Maua","Msichana","gari","Tehama","Kimbia"]
    word = random.choice(orodha_chaguo)
    display_l = len(word)
    display = "_" * display_l
    zilizo_chaguliwa = []
    count = 0


#loop game
def loop_game():
    global play_game
    play_game = input("Tafadhali kama unaitaji kurudia kucheza game jibu 'Y' au  'N' kuacha klucheza : ")
    while play_game not in ["y","n"]:
          play_game = input("Tafadhali kama unaitaji Xx kurudia kucheza game jibu 'Y' au  'N' kuacha klucheza : ")
    if play_game == "y":
          main()
    elif play_game == "n":
            print(f"asante kwa kucheza game hii karibu tena ndugu {name} \n")
            exit()

#eng_game  
def hangman():
    global display
    global word
    global count
    global zilizo_chaguliwa
    limt = 5
    jaribu = input(f"heey {name} bashiri herufi za neno {display} \n")
    jaribu =jaribu.strip()
    if len(jaribu.strip()) != 1:
        print(f"ohhh samahani {name} nadhani umekosea tafadhari jaribu tena \n")
        hangman()
    elif jaribu in word:
        zilizo_chaguliwa.extend([jaribu])
        index = word.find(jaribu)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + jaribu + display[index + 1:]
        print(f"{display} \n")
    elif jaribu in zilizo_chaguliwa:
        print("\n sawa andika herufi nyingine \n")
    else:
        count += 1
      
        if count == 1:
            time.sleep(1)
            print(f"ohh samahani ndugu {name} umekosea. lakini husijari umebakiza mara  {str(limt - count)} za kujalibu tena \n")
    
        elif count == 2:
            time.sleep(1)
            print(f"ohh samahani ndugu {name} umekosea. lakini husijari umebakiza mara  {str(limt - count)} za kujalibu tena \n")
    
        elif count == 3:
            time.sleep(1)
            print(f"ohh samahani ndugu {name} umekosea. lakini husijari umebakiza mara  {str(limt - count)} za kujalibu tena \n")
    
        elif count == 4:
            time.sleep(1)
            print(f"ohh samahani ndugu {name} umekosea. lakini husijari umebakiza mara  {str(limt - count)} za kujalibu tena \n")
    
        elif count == 5:
            time.sleep(1)
            print(f"ohh samahani ndugu {name} umekosea. \n")
            print(f"jibu lilikua ni {word}")
            loop_game()
    if word == "_" * display_l:
        print(f"ongera sana {name} umeshinda ")
        loop_game()
    elif count != limt:
        hangman()

main()
hangman()
import random
my_no=random.randint(1,100)

intro="""
                                                                                                                                                                                                       
                                                                                                                                            
 ▄▄   ▄ ▄    ▄ ▄    ▄ ▄▄▄▄▄  ▄▄▄▄▄▄ ▄▄▄▄▄           ▄▄▄  ▄    ▄ ▄▄▄▄▄▄  ▄▄▄▄   ▄▄▄▄  ▄▄▄▄▄  ▄▄   ▄   ▄▄▄           ▄▄▄    ▄▄   ▄    ▄ ▄▄▄▄▄▄
 █▀▄  █ █    █ ██  ██ █    █ █      █   ▀█        ▄▀   ▀ █    █ █      █▀   ▀ █▀   ▀   █    █▀▄  █ ▄▀   ▀        ▄▀   ▀   ██   ██  ██ █     
 █ █▄ █ █    █ █ ██ █ █▄▄▄▄▀ █▄▄▄▄▄ █▄▄▄▄▀        █   ▄▄ █    █ █▄▄▄▄▄ ▀█▄▄▄  ▀█▄▄▄    █    █ █▄ █ █   ▄▄        █   ▄▄  █  █  █ ██ █ █▄▄▄▄▄
 █  █ █ █    █ █ ▀▀ █ █    █ █      █   ▀▄        █    █ █    █ █          ▀█     ▀█   █    █  █ █ █    █        █    █  █▄▄█  █ ▀▀ █ █     
 █   ██ ▀▄▄▄▄▀ █    █ █▄▄▄▄▀ █▄▄▄▄▄ █    ▀         ▀▄▄▄▀ ▀▄▄▄▄▀ █▄▄▄▄▄ ▀▄▄▄█▀ ▀▄▄▄█▀ ▄▄█▄▄  █   ██  ▀▄▄▄▀         ▀▄▄▄▀ █    █ █    █ █▄▄▄▄▄
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
"""
intro2=R"""

   ___                       _____ _                __                 _               
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                                       
                                                                                       
                                                                                       
"""
line1="""
Welcome To NUMBER GUESSING GAME
Currently I'm thinking of a number Between range [1-100]


"""


print(intro)
print(line1)
d=input("Choose Difficulty: Easy or Hard :")
attempt=10
if d.lower()== "hard":
    attempt=5
line2=f"You Have {attempt} Chances To Guess The Number"
line4=f"You Lose, Number Was {my_no}"
print(line2)
print(intro2)
print()
print()
R1=("Too High","Too Low","High","Low",f"You Got It!!! Number Was {my_no}")
while attempt:
    line3=f"You Have {attempt} Chance Left"
    print(line3)
    try:
        user_no: int = int(input("Your Guess : "))
        diff=user_no-my_no
        if(diff<0):
            ans=3
            if diff<=-15:
                ans=1
        elif diff>0:
            ans=2
            if(diff>=15):
                ans=0

        else:
            ans=4
            print(R1[ans])
            break

        print(R1[ans])
        attempt-=1
    except:
        print("Please Enter Valid Number")

if attempt==0:
    print(line4)
input("press enter to close window")


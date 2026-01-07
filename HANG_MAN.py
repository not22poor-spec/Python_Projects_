import random
print(r""" _   _                                      ___  ___              _   _ 
| | | |                                     |  \/  |             | | | |
| |_| | __ _ _ __   __ _                    | .  . | __ _ _ __   | | | |
|  _  |/ _` | '_ \ / _` |                   | |\/| |/ _` | '_ \  | | | |
| | | | (_| | | | | (_| |                   | |  | | (_| | | | | |_| |_|
\_| |_/\__,_|_| |_|\__, |                   \_|  |_/\__,_|_| |_| (_) (_)
                    __/ |  ______   ______                              
                   |___/  |______| |______|                             """)


def level(i):
    if i==0:
        print(R'''                 +---+
                 |   |
                     |
                     |
                     |
                     |
                 =========''')
    elif i==1:
        print(R'''                 +---+
                 |   |
                 O   |
                     |
                     |
                     |
                 =========''')
    elif i==2:
        print(r'''                 +---+
                 |   |
                 O   |
                 |   |
                     |
                     |
                =========''')
    elif i==3:
        print(r'''                 +---+
                 |   |
                 O   |
               / |   |
                     |
                     |
                =========''')
    elif i==4:
        print(r'''                 +---+
                 |   |
                 O   |
               / | \ |
                     |
                     |
                =========''')
    elif i==5:
        print(r'''                 +---+
                 |   |
                 O   |
               / | \ |
                /    |
                     |
                =========''')
    elif i==6:
        print(r'''+---+
                 |   |
                 O   |
               / | \ |
                / \  |
                     |
                =========''')
        print()
        print()
        print()
        print(r'''                        __           _    
 _   _  ___  _   _     / /  ___  ___| |_  
| | | |/ _ \| | | |   / /  / _ \/ __| __| 
| |_| | (_) | |_| |  / /__| (_) \__ \ |_  
 \__, |\___/ \__,_|  \____/\___/|___/\__| 
 |___/                                    ''')
    return 0
wordlist=('python', 'javascript', 'challenge', 'beautiful', 'adventure', 'mystery',
    'galaxy', 'universe', 'mountain', 'waterfall', 'hurricane', 'volcano',
    'elephant', 'giraffe', 'penguin', 'crocodile', 'dolphin', 'butterfly',
    'computer', 'keyboard', 'algorithm', 'software', 'network', 'database',
    'symphony', 'orchestra', 'apple', 'banana', 'grape', 'lemon', 'mango', 'peach', 'pear', 'orange',
    'house', 'chair', 'table', 'door', 'clock', 'phone', 'light', 'book',
    'spoon', 'fork', 'plate', 'bowl', 'bread', 'water', 'milk', 'juice',
    'sugar', 'pizza', 'cake', 'salad', 'soup', 'cheese', 'lion', 'tiger',
    'bear', 'horse', 'monkey', 'snake', 'frog', 'fish', 'bird', 'duck',
    'wolf', 'sheep', 'mouse', 'puppy', 'kitten', 'hand', 'foot', 'head',
    'face', 'hair', 'eyes', 'nose', 'ears', 'mouth', 'heart', 'arm', 'leg',
    'boat', 'train', 'plane', 'truck', 'road', 'park', 'ball', 'game',
    'team', 'play', 'walk', 'jump', 'swim', 'sing', 'read', 'write',
    'draw', 'talk', 'work', 'help', 'blue', 'red', 'green', 'yellow',
    'black', 'white', 'pink', 'brown', 'sun', 'moon', 'star', 'tree',
    'leaf', 'rock', 'rain', 'snow', 'wind', 'fire', 'river', 'dream',
    'smile', 'happy', 'music', 'sound','xylophone', 'jazz', 'rhythm', 'melody',
    'chocolate', 'spaghetti', 'avocado', 'strawberry', 'pineapple', 'broccoli',
    'architect', 'scientist', 'astronaut', 'detective', 'engineer', 'librarian',
    'pyramid', 'sphinx', 'colosseum', 'acropolis', 'monument', 'sculpture',
    'oxygen', 'hydrogen', 'molecule', 'gravity', 'satellite', 'telescope',
    'treasure', 'journey', 'expedition', 'discovery', 'champion', 'victory',
    'amazing', 'fantastic', 'wonderful', 'gorgeous', 'vibrant', 'brilliant',
    'carnival', 'festival', 'celebration', 'parade', 'holiday', 'vacation',
    'knowledge', 'wisdom', 'education', 'university', 'library', 'dictionary',
    'bicycle', 'motorcycle', 'helicopter', 'submarine', 'zeppelin', 'hovercraft',
    'wizard', 'dragon', 'phoenix', 'unicorn', 'goblin', 'magic',
    'puzzle', 'riddle', 'enigma', 'cipher', 'labyrinth', 'paradox',
    'zucchini', 'cinnamon')
stage=0
wordno=random.randint(0,199)
length=len(wordlist[wordno])
word=list(wordlist[wordno])
level(stage)
guessword=list()
print(f"length of word {length}")
print("\n\t\tYour Word is: ",end="")
for i in range(length):
    print("_",end="")
    guessword.append('')
print()
while stage<=6:
    guess = (input('ENTER LETTER :'))
    guess=guess.lower()
    if guess in word:
        for j in range(length):
            if word[j]==guess:
                guessword[j]=word[j]
    else:
        stage+=1

    level(stage)
    print("\n\t\tYour Word : ", end="")
    for i in guessword:
        if i=="":
            print("_", end="")
        else:
            print(i,end="")
    print()
    if str(word)==str(guessword):
        print("VICTORY")
        break
    if(level==6):
        break
print(word)
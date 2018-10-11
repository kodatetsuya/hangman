import random

def hangman():
    w_list=["unko","apple","banana","meat","rice"]
    word=random.choice(w_list)
    wrong=0
    stages=["",
            "_________         ",
            "|                 ",
            "|        |        ",
            "|        0        ",
            "|       /|\       ",
            "|       / \       ",
            "|                 "
            ]
    r_letters=list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to Hangman!")
    while wrong<len(stages)-1:
        print("\n")
        char=input("Guess a letter:")
        if char in r_letters:
            n=r_letters.index(char)
            board[n]=char
            r_letters[n]="$"
        else:
            wrong +=1
        print(" ".join(board))
        print("\n".join(stages[0:wrong+1]))
        if "_" not in board:
              print("You win!")
              print(" ".join(board))
              win=True
              break
    if win==False:
              print("\n".join(stages[0:wrong+1]))
              print("You lose! The word is {}.".format(word))

hangman()               

# print("\n".join(stages[0:len(stages)]))


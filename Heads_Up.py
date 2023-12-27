import random

#naming the file from where we generate random words
FILE_NAME="cswords.txt"

def get_words_from_file():
    f=open(FILE_NAME)
    lines=[]
    for line in f:
        line=line.strip() #removing whitespace characters
        if line!="": #checking if line is empty or not, if it is empty then skip it
            lines.append(line) #putting words in an empty list
    return lines
    
#generating random words
def play_game(words,start):
    while start=="":
        random_word=random.choice(words)
        print(random_word)
        start=input()
    output=["exit","Exit","EXIT"]
    if start in output:
        print("Thanks for playing!")
    else:
        print("Invalid Input!")

def main():
    print("** HEADS UP **")
    print("")
    print("How to play?")
    print("Press Enter to play the game!")
    print("Enter Exit to stop playing.")
    words=get_words_from_file()
    start=input()
    output=["EXIT","Exit","exit"]
    if start=="":
        play_game(words,start)
    elif start in output:
        print("Thanks for playing!")
    else:
        print("Eror!")
    
if __name__ == '__main__':
    main()

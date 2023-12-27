import random

# list of random words
words=["elephant","window","leaf","snake","table","chair","skateboard","lips","fire","lion","candy","triangle","cup","Mickey Mouse","bumblebee","moon","desk","snail","blocks","bug","candle","giraffe","chicken","baby","zebra","bunk", "bed","rain","bread","grass","feather","nail","pie","bee","alive","popsicle","pants","bone","shirt","horse","jail","jacket","broom","mouse","box","ghost","fork","arm","bear","airplane","crack"]
    
def main():
    print(">> GUESS THE WORD <<")
    random_word=random.choice(words) # generating a random word from the list
    real_word=[]
    for letter in random_word:
        real_word.append(letter) # adding the word in a list
    print("")
    length=len(real_word)
    guesses=length*2 # number of guesses would be twice the length of the word
    print("It is a "+ str(length)+ " letter word")
    print("You get "+ str(guesses)+ " guesses")
    secret_word=[]
    for i in range(length):
        secret_word.append("_") # making the secret word with underscores
    for j in secret_word:
        print(j,end=" ") 
    print("")
    
    # game starts here
    
    for k in range(guesses,0,-1):
        guess=input("Type a single letter here, then press enter:")
        print("The word now looks like this:",end=" ")
        for i in range(len(real_word)):
            if real_word[i]==guess:
                secret_word[i]=real_word[i] # adding the guessed word in the same index
            else:
                continue # skipping if its not in the real word
        for m in secret_word:
            print(m,end=" ")
        print("")
        # checking if its the last guess or not
        
        if k!=1: # when its not the last guess
            if secret_word!=real_word:
                print("You have "+ str(k-1)+ " guesses left!") # notifying the user
            else:
                print("") 
                print("Congratulations! You guessed the word correctly.")
                print("The word was",random_word)
                break
        else: # in case of last guess
            if secret_word!=real_word:
                print("")
                print("Oops! You couldn't guess the word.")
                print("The word was",random_word)
            else:
                print("")
                print("Congratulations! You guessed the word correctly.")
                print("The word was",random_word)
    
    print("")
    print("Thanks for playing!") # ending the game
    
main()

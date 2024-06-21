import random # Random

# First create a function that reads WORDS from a file & prompts as a list.
def wordReference(file_path): ## this takes a single parameter, define as filepath which will be the path where the words are located @.
    with open(file_path) as pathToFile: # to gain access to the file, we have to OPEN it. Using the WITH STATEMENT & open function which basically is a fetch kind of thing.
        words = [line.strip() for line in pathToFile] # TO process the file, im requesting the computer to go line by line in the file.
    return words # this will return the "WORDS" , "TERMS" in said list file

def userGuess(uGuess, theGuesses): ## Producing a function for guessing. There's a list dedicated to acceptable guesses.
    return len(uGuess) == 5 and uGuess in theGuesses #len is a built in function for length / num of items in container.
# ^^ this line returns which the computer will observe if condition is T or F . There are two objective of checking
#computer will check the length of the user guess and it must be 5 characters. ; the uguess is then checked if it matches in "theGuesses".txt file.

def obsUguess(uGuess, word): # calling function obsUguess (observe user guess) , this take two parameters : userguess, and word (correct secret word)
    wordGuess= "" #initializing an empty string. This will assist and connect the guess word & observe the word itself and identify if the word is close to key or not.
    for i in range(5): # Loop each letter , the word is 5 letters.
        #/033 is a key that allows text formatting.
        if uGuess[i] == word[i]: # this basically compares the uGuess & the key word.
            wordGuess += "\033[94m" + uGuess[i] #94m = light blue ; light blue will letters that are in the correct position.
        else:
            if uGuess[i] in word:
                wordGuess += "\033[95m" + uGuess[i] #95 = light pink , if the letter is correct & wrong position.;
            else:
                wordGuess += "\033[91m" + uGuess[i] #91 = Red ; incorrect letter in the word.
    return wordGuess + "\033[0m" #0m is default color , it just does a whole reset on a new word and if it has not correlation to correct queues.

def GTW(guesses, answers): #GTW , GUESS THE WORD - two parameters thrown: guesses and answer.
    print("★★GUESS THAT 5 LETTER WORD!★★") # INTRODUCING the game.
    theSecret = random.choice(answers).lower() # this will queue the game to choose a random word through the answer list.
    #.choice is a function in python in random module.
    tries = 1 # this basically tracks the tries, we will == 1 to indicate the first try
    maxTries = 4 # providing x amount of tries.
    while tries <= maxTries:
        guess = input("Enter word for guess #" + str(tries) + ": ").lower() # tracking number of guess , in this input.
        if not userGuess(guess, guesses): # checks  if the guess is valid , comparing guess and the guesses.
            print("Hmm nice try, please enter another 5 letter word that's valid .")
            continue #continue is to skip the rest of loop and go back to asking for another guess
        if guess == theSecret: # if the user guess is == to the secret key this happens:
            print("Yay yay you did it! You guess the secret word:", theSecret)
            break # loop then breaks.
        tries += 1 #this tracks the amount of tries the user has taken.
        theResponse = obsUguess(guess, theSecret) # the response = the function of obsUguess which does a compare from the guess to the key.
        print(theResponse) #this will show the feedback of that guess and it will prompt the word in color coded manner which is tied to again the function of obsUguess
    if tries > maxTries:#if the amount of tries goes over the max  tries, this happens:
        print("GAME OVER! Maybe next time. The word is: ", theSecret)

def GuessTheWord(): #all in one function to run the code code.
        guesses_dictionary = "theGuesses.txt" #AI created List
        answers_dictionary = "theAnswers.txt" #AI created list
        guesses = wordReference(guesses_dictionary) # this is where variable guesses stems from
        answers = wordReference(answers_dictionary) # this is where the variable answers stems from
        GTW(guesses, answers) #Calling the GTW function that passes guesses & answers. This basically funciton the list that run the word guessing game.

import random
import time
from Hangman_ascii import number_wrong
 
def again():
    
    c = 0
    while c == 0:
        again = input('Do you want to play again? (y/n)  ')
        again = again.lower()
        if again == 'y':
            c = c + 1
            initalisation()
        elif again == 'n':
            c = c + 1
            time.sleep(1)
            exit()
        else:
            continue

def player():
    global length, theme, word, word_reveal
    x = False
    while x == False:
        word = input('\nInput a word here:   ')
        word = word.lower()
    
        x = str.isalpha(word)
        if x == False:
            print("ERROR: Input a Word, with no letters or symbols")
    
    theme = input('What is the theme of your word?   ')
    print('\n'*65)
    length = len(word)
    
    playerinput()
    
def computer():
    global length, word

    while True:
        try:
            length = int(input('How long do you want the word to be?   '))
            fo = open ("appFiles/words.txt", "r")
            yo = fo.readlines()

            ranlist = []
            for y in range(len(yo)-1):
                y = y + 1
                if len(yo[y]) == (length+1):
                    ranlist.append(yo[y])
        
            rannum = (random.randint(0, (len(ranlist))))
            word = (ranlist[rannum])
            break
        except ValueError:
            print("ERROR: Not a valid integer")
        except IndexError:
            print('Error: Not in the range, pick a number that is less than 12 letters')

  
    playerinput()
    

def playerinput():
    
    global correct, word_reveal, guess
    letters = []

    print ('\nHow many incorrect guesses do you want?' )
    
    while True:
        try:
            tries = int(input('A Standard Game of Hangman end after 9 inccorect guesses   '))
            break
        except ValueError:
            print("ERROR: Not a valid integer")
                        
                        
    try:
        theme
        print ('\nThe theme is,',theme)
    except NameError:
        pass
        
    print ('\nThe word is',length,'letters long!')
    print('_ '*length)

    false = 0
    correct = 0

    word_reveal = ['_']*length

    while false <= tries:
        guess = input('\nWhat letter or word do you want to input:' + '   ')
        guess = guess.lower()
        
        if len(guess) == length:
            if guess == word:
                print("You have correctly guessed the word!")
                again()
                    
        elif guess == ' ':
            print("ERROR: Space isnt a valid input")
    
        elif guess in letters:
            print("ERROR: You have already guessed that")
            continue
        
        letters.append(guess)
        print ("\nYou've guessed:  " +" ".join(letters))
        
        if guess in word:
            print ('\nCorrect Guess\n')
            x = 0
            for i in range(len(word)):
                new_word = word.replace(guess,"_", x)
                new_result = new_word.find(guess)
                int(new_result)
                
                if new_result >= 0:
                    word_reveal[new_result] = guess
                    i = i + 1
                    x = x + 1
                    correct = correct + 1
            print(' '.join(word_reveal))

               
            if correct == length:
                print ('Well Done! You guessed correctly')
                again()
                    
        elif guess not in word:
            print ('Incorrect Guess')
            
            if tries == 9:
                print (number_wrong[false], '\n')
            print(' '.join(word_reveal))

            false = false + 1
            
            if false == tries:
                print ('Out of Guesses!')
                print('The Word was: ',word,'\n')
                again()
                
def initalisation(): 
    x = False

    while x == False:
        mode = input('\nDo you want to play against the computer or have another player input a word?   ')
        mode = mode.lower()
        
        x = str.isalpha(mode)
        if x == False:
            print("ERROR: Input either 'player' or 'computer'")
            
    if mode == 'player' or mode == 'p' or mode == 'players':
        player()
    elif mode == 'computer' or mode == 'c' or mode == 'computers':
        computer()
    else:
        initalisation()
initalisation()
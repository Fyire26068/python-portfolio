import random
#Anthony Garrard
#hangman game
#10/20
hangman = ('''
      _________________
      ||            ||
      ||            ||
     _||_           ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',#creating graphics for game
'''
      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (o_o)          ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',
'''
      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (o_o)          ||
      | |           ||
      | |           ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',
'''
      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (o_o)          ||
    //| |           ||
   // | |           ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',
'''
      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (o_o)          ||
    //| |\\\\         ||
   // | | \\\\        ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',
'''
      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (o_o)          ||
    //| |\\\\         ||
   // | | \\\\        ||
     //             ||
    //              ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',
'''

      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (o_o)          ||
    //| |\\\\         ||
   // | | \\\\        ||
     // \\\\          ||
    //   \\\\         ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''',
           '''

      _________________
      ||            ||
      ||            ||
     _||_           ||
      /}\           ||
     (#_#)          ||
    //| |\\\\         ||
   // | | \\\\        ||
     // \\\\          ||
    //   \\\\         ||
                    ||
                    ||
                    ||
                    ||
                    ||
____________________||___''')

wordBank = ["STRING", "ARRAY", "INTEGER", "FLOAT", "PYTHON", "PROGRAM", "CODE",
            "KEYBOARD","TYPE", "MOUSE", "COMPUTER", "CHARACTER", "MONITOR",
            "GOOGLE", "WHILE", "LOOP", "FOR", "OR", "AND", "DISPLAY",
            "PRINT", "LOGIC"]#word bank
wrong = 0
hangmanDisplay = hangman[wrong]
word = random.choice(wordBank)
#print(word)
      
wordLen = len(word)
blanks = '-' * wordLen
wordDisplay = list(blanks)
startingPos = 0
letterBank = list('-' * 26)
bankPos = 0

print("\n------------------\nWelcome to Hangman\n------------------\n")

while hangmanDisplay != hangman[7]: #logic for guess
    charPos = -1#resetting character position
    
    print(str(hangmanDisplay) + "\n")#printing screen
    print("Word: " + str(wordDisplay) + "\n")
    print(str(letterBank) + "\n")
          
    guess = input("Guess a Letter : ")#getting guess from player
    guess = guess.upper()   
    
    if len(guess) == 1 and guess >= 'A' and guess <= 'Z': #making sure guess is a vailid response
        if guess not in letterBank: #making sure guess has not been guessed before  
            letterBank[bankPos] = guess #adding guess to the letter bank
            bankPos = bankPos +1 #moving the bank position up 1
            if guess in word: #checking if guess is in the word
                print("\nYour guess is in the word.\n")
                for i in range(startingPos,wordLen): #replacing wordDisplay letters with the correctly guessed letters
                    charPos = word.find(guess, charPos+1)
                    if word[charPos] == guess:
                        wordDisplay[charPos] = guess  
            else: #altering hangman display
                print("\nYour guess is not in the word\n")
                wrong = wrong +1
                hangmanDisplay = hangman[wrong]
        else: #if they already guessed the letter
            print("\n-------------------------------\nYou already guessed that letter\n-------------------------------\n")
    else: #if its an invalid response
        print("\n----------------\nInvalid Response\n----------------\n")
        
    if '-' not in wordDisplay: #checking for win
        print(hangmanDisplay)
        print("\nYou won, the word was : " + word + "\n")
        break
    
if hangmanDisplay == hangman[7]: #making sure its a loss
    print(hangmanDisplay)
    print("\nYou lost, the word was : " + word + "\n")
input()

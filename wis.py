import random
hangman = ["""
        +---+
        |   |
            |
            |
            |
            |
    =========    
        """, """
        +---+
        |   |
        O   |
            |
            |
            |
    =========    
        """, """
        +---+
        |   |
        O   |
        |   |
            |
            |
    =========    
        ""","""
        +---+
        |   |
        O   |
       /|   |
            |
            |
    =========    
        ""","""
        +---+
        |   |
        O   |
       /|\  |
            |
            |
    =========    
        ""","""
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
    =========    
        ""","""
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
    =========    
        """]
words = 'welcome to home'.split()
def getRandomWord(wordList):
    wordIndex= random.randint(0, len(wordList)-1)
    return wordList[wordIndex]
def displayBoard(handman, missedLetters,correctLetters, secretWord):
    print(handman[len(missedLetters)])
    print()

    print("Wrong letter:", end = "")
    for letter in missedLetters:
        print(letter, end = '')
    print()

    blanks='*'*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks=blanks[:i]+blanks[i+1:]
    for letter in blanks:
        print(letter, end = '')
    print()
def getGuess(alreadGuessed):
    while True:
        print("Write letter please:")
        guess = input()
        guess= guess.lower()
        if len(guess)!= 1:
            print("Again write letter please")
        elif guess in alreadGuessed:
            print("Try again choice letter")
        else:
            return guess
def playAgain():
    print('Do you want play game again?: ("Yes" or "No")')
    return input().lower().startswith('y')
print("H A N D M A N")
missedLetters=''
correctLetters=''
secretWord=getRandomWord(words)
gameIsDone=False

while True:
    displayBoard(hangman, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters+correctLetters)
    if guess in secretWord:
        correctLetters=correctLetters+guess
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
                break
        if foundAllLetters:
            print("Great! You are win! " + secretWord)
            gameIsDone=True
    else:
        missedLetters= missedLetters+ guess
        if len(missedLetters)==len(hangman)-1:
            displayBoard(hangman, missedLetters, correctLetters, secretWord)
            print("You have not try\n"+ str(len(missedLetters)) + "mistake\n" + str(len(correctLetters)+ "right letters\n"+secretWord) )
            gameIsDone=True

    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone= False
            secretWord=getRandomWord()
        else:
            break


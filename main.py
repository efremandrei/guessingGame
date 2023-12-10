import random, time

expressionsList = [['always', 'deliver', 'quality'],
                   ['ask', 'powerful', 'questions'],
                   ['audit', 'your', 'metrics'],
                   ['based', 'on', 'results'],
                   ['be', 'the', 'communication'],
                   ['friends', 'are', 'treasures'],
                   ['health', 'is', 'wealth'],
                   ['just', 'be', 'awesome'],
                   ['knowledge', 'is', 'power'],
                   ['keep', 'it', 'simple']
                   ]
playAgain = True
while playAgain:
    # choose on of the expressions
    chosenExpression = expressionsList[random.randint(0, len(expressionsList)-1)]
    #debugging print:
    #print(chosenExpression)
    parallelList = []
    # Create another list just made out of '_'s
    for word in chosenExpression:
        parallelList.append('_'*len(word))
    #debugging print:
    #print(parallelList)

    oneStringUnderscores = ' '.join(parallelList)
    oneStringExpression = ' '.join(chosenExpression)

    score = 0
    startTime = 0
    print("To exit the game mid-game, enter 'exit' instead of a character")
    startTime = time.time()
    while '_' in oneStringUnderscores:
        guess = input(f'The expression is "{oneStringUnderscores}", please guess a character! \n')
        #to exit game mid-game
        if guess == 'exit':
            print("Thanks for playing, hope you had fun! BYE!")
            break
        #If the user entered a multi-character string
        if len(guess) > 1:
            print("Cheater cheater pants on...fire? \n Anyway, please enter only ONE character at a time!")
            continue
        #If the user entered a non-letter character (number or symbol)
        if not guess.isalpha():
            print("Hmmm, Please guess LETTERS ONLY\n")
            continue
        #if the letter is correct and wasnt guessed before
        if guess in oneStringExpression and guess not in oneStringUnderscores:
            print("Good guess!\n")
            score +=5
            indicesOfGuess = [index for index, char in enumerate(oneStringExpression) if char == guess]
            for i in indicesOfGuess:
                oneStringUnderscores = oneStringUnderscores[:i] + guess + oneStringUnderscores[i+1:]
        #if the letter was guessed before
        elif guess in oneStringUnderscores:
            print("Hey cheater! you've done that already! try something new!")
            continue
        #a letter that is not in the string
        elif guess not in oneStringExpression:
            print("Nice try, not good enough though, let's try again...")
            score -=1
    if guess != 'exit':
        #if expression was guessed correctly withing 30 seconds a bonus of 100 points is given
        if (time.time()-startTime) < 30:
            print("You guessed right very fast! Get a bonus of 100 points! \n")
            score += 100
        print(f'Congratulation! you\'ve guessed the whole expression!\n it\'s: "{oneStringExpression}"\n '
              f'And your score is: {score}\n')
    #while the user didn't enter Y or N, he'll be prompted again and again
    while playAgain != 'Y' or playAgain != 'N':
        playAgain = input("Would you like to play another round?(Y/N) \n")
        #The user doesn't want to continue for another round, exiting game
        if playAgain == 'N':
            playAgain = False
            print("thanks for playing the game...Bye bye!\n")
            break
        #The user wants to play once more
        elif playAgain == 'Y':
            playAgain = True
            print("Ok, so we're playing another round!\n")
            startTime = time.time()
            break

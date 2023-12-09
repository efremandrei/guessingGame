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
    print(chosenExpression)
    parallelList = []
    # Create another list just made out of '_'s
    for word in chosenExpression:
        parallelList.append('_'*len(word))
    print(parallelList)

    oneStringUnderscores = ' '.join(parallelList)
    oneStringExpression = ' '.join(chosenExpression)

    score = 0
    startTime = 0
    while '_' in oneStringUnderscores:
        startTime = time.time()
        guess = input(f'The expression is "{oneStringUnderscores}", please guess a character! \n')
        if guess == 'exit':
            print("Thanks for playing, hope you had fun! BYE!")
            break
        if len(guess) > 1:
            print("Cheater cheater pants on...fire? \n Anyway, please enter only ONE character at a time!")
            continue
        if not guess.isalpha():
            print("Hmmm, Please guess LETTERS ONLY\n")
            continue
        if guess in oneStringExpression and guess not in oneStringUnderscores:
            print("Good guess!\n")
            score +=5
            indicesOfGuess = [index for index, char in enumerate(oneStringExpression) if char == guess]
            for i in indicesOfGuess:
                oneStringUnderscores = oneStringUnderscores[:i] + guess + oneStringUnderscores[i+1:]
        elif guess in oneStringUnderscores:
            print("Hey cheater! you've done that already! try something new!")
            continue
        elif guess not in oneStringExpression:
            print("Nice try, not good enough though, let's try again...")
            score -=1
    if guess != 'exit':
        if time.time()-startTime < 30:
            print("You guessed right very fast! Get a bonus of 100 points! \n")
            score += 100
        print(f'Congratulation! you\'ve guessed the whole expression!\n it\'s: "{oneStringExpression}"\n '
              f'And your score is: {score}\n')

    while playAgain != 'Y' or playAgain != 'N':
        playAgain = input("Would you like to play another round?(Y/N) \n")
        if playAgain == 'N':
            playAgain = False
            print("thanks for playing the game...Bye bye!\n")
            break
        elif playAgain == 'Y':
            playAgain = True
            print ("Ok, so we're playing another round!\n")
            break
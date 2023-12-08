import random

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

while '_' in oneStringUnderscores:
    guess = input(f'The expression is {oneStringUnderscores}, please guess a character!')
    if guess in oneStringExpression and guess not in oneStringUnderscores:
        print("Good guess!/n")
        indicesOfGuess = [index for index, char in enumerate(oneStringExpression) if char == guess]
        for i in indicesOfGuess:
            oneStringUnderscores = oneStringUnderscores[:i] + guess + oneStringExpression[i+1:]
    elif guess in oneStringUnderscores:
        print("Hey cheater! you've done that already! try something new!")
        continue
    elif guess not in oneStringExpression:
        print("Nice try, not good enough though, let's try again...")
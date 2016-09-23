import random

pool = ["YESTERDAY", "REMEMBER", "EXCLAMATION", "PRETEND", "SURROUND", "INTERESTING", "JEALOUSY", "LOGARITHMIC"]
letterGuess = 0
wordGuess = 0
count = 0
attempt = "N"
solved = "N"
badGuesses = []
body = "o|--<"


word = random.choice(pool)
print "The word is %r letters long." % str(len(word))
print "You are of sound mind and body! %r " % body
solution = list(word)
hiddenSolution = ["_"] * len(solution)
print hiddenSolution

while (solved == "N") and (count < 5):
    letterGuess = str.upper(raw_input("What letter do you guess? "))
    if letterGuess in solution:
        print "You got one!"
        #this tells the player if the letter shows up in the word and how many times
        #print "%r shows up %r times in the word." % (letterGuess, solution.count(letterGuess))
        #this tells the player where the letter shows up in the word
        for i, j in enumerate(solution):
            if j == letterGuess:
                hiddenSolution[i] = j
                print "%r shows up at postion %r." % (letterGuess, i)
                print hiddenSolution
        #this asks if the player can guess the word
        attempt = str.upper(raw_input("Can you guess the word (Y or N)? "))
        if attempt == "Y":
            wordGuess = str.upper(raw_input("What's the word? "))
            if wordGuess == word:
                solved = "Y"
                print "You won! The word is in fact %r." % word
                break
            else:
                print "Nope. Try again"
        else:
            continue
    else:
        badGuesses.append(letterGuess)
        count += 1
        body = body[:-1]
        print "Boo! Boo! %r doesn't show up in the word. Your number of incorrect guess is %r" % (letterGuess, count)
        print "Also. You've lost a body part! Ouchie!"
        print body
        print badGuesses

if count == 5:
    print "Your are dead. Dead. Dead. Sorry."
    print "The word was %r" % word

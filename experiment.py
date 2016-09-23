import random

pool = ["YESTERDAY", "REMEMBER", "EXCLAMATION", "PRETEND", "SURROUND", "INTERESTING", "JEALOUSY", "LOGARITHMIC"]

word = random.choice(pool)
print word
solution = list(word)
print solution
print "There are %r letters in %r." % (len(word), word)

# this changes the list of word letters to _ so the player can see a visual representation of the word without the letters#
hiddenSolution = ["_"] * len(solution)
print hiddenSolution

letterGuess = "Y"
for i, j in enumerate(solution):
    if j == letterGuess:
        hiddenSolution[i] = j
        print "%r shows up at postion %r." % (letterGuess, i)
        print hiddenSolution

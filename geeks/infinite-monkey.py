import random

def generateOne(length):
    str = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    for i in range(length):
        str+=(alphabet[random.randrange(27)]) 
    return str

def score(goal, teststring):
    match = 0
    for c in range(len(goal)):
        if goal[c] == teststring[c]:
            match+=1
    return (match/len(goal))*100

def main():
    maxScore = 0
    goalstring = "methinks it is like a weasel"
    newString = generateOne(28)
    newScore  = score(goalstring, newString)
    print(newString, newScore)
    while newScore < 100:
        if newScore > maxScore:
            maxScore =  newScore
            print(newString, newScore)
        newString = generateOne(28)
        newScore  = score(goalstring, newString)
main()

from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s= Stack()
    balanced =True
    index = 0
    opening = '({['
    while (index< len(symbolString)) and balanced:
        if symbolString[index] in opening:
            s.push(symbolString[index])
        else:
            if s.isEmpty():
                balanced = False
            else:
                balanced = isMatch(s.pop(), symbolString[index])
        index+=1
    return s.isEmpty() and balanced

def isMatch(open, close):
    openings = '({['
    closings = ')}]'
    return openings.index(open) == closings.index(close)

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))

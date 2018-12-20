def anticlock(string1, string2):
    if len(string1)!=len(string2): return False
    for i in range(0,len(string1)):
        if (string1[i] != string2[(i+2)%len(string1)]):
            return False
    return True

def clock(string1, string2):
    if len(string1)!=len(string2): return False
    for i in range(0,len(string1)):
        if (string2[i] != string1[(i+2)%len(string1)]):
            return False
    return True

string1 = "amazon"
string2 = "azonamw"

print (anticlock(string1, string2) or clock(string1, string2))

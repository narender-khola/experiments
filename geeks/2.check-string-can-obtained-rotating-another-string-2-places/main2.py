string1 = "amazon"
string2 = "azonam"

anticlock = "" + string1[2:] + string1[0:2]
clock = "" + string1[-2:] + string1[0:-2]

print anticlock == string2 or clock == string2

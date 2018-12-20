def LIS(A):
    lis = [1 for i in range(len(A))]
    for i in range(1,len(A)):
        max =0
        for j in range(0,i):
            if(A[j]< A[i]) and lis[j]>max:
                max = lis[j]
        if max > 0:
            lis[i] = max + 1
    return lis[len(A)-1]

def ceil_index(A, val):
    l=0
    r= len(A) -1
    while(r-l>1):
        m = (l+r)/2
        if A[m]>=val:
            r=m
        else:
            l=m
    return r


A = [1,2,3,4,9,9,8,5,6,7]
lis = [0 for i in range(len(A)+1)]
lis[0] = A[0]
length = 1
for j in range(1,len(A)):
    if A[j] < lis[0]:
        lis[0]=A[j]
    elif A[j] > lis[length-1]:
        lis[length]=A[j]
        length+=1
    else:
        index = ceil_index(A,A[j])
        lis[index] = A[j]

print lis
print length
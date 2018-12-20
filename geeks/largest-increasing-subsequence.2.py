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



A = [1,2,3,4,9,9,8,5,6,7]
print LIS(A)
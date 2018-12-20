def LIS(A, n):
    if n == 0:
        return 1
    max_ending_here = 1
    for j in range(n):
        if A[j] < A[n]:
            res = LIS(A,j)
            max_ending_here = max(max_ending_here, res+1)
    return max_ending_here

def max(a,b):
    return a if a>b else b

A = [1,2,3,4,9,9,8,5,6,7]
print LIS(A, len(A)-1)
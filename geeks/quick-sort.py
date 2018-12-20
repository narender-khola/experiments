
def quick_sort(A, l, r):
    if l < r:
        pivot = r
        i = l
        while(i<pivot):
            if A[i] > A[pivot]:
                swap(A, pivot-1, i)
                swap(A, pivot-1, pivot)
                pivot-=1
            else:
                i+=1
        quick_sort(A,l, pivot-1)
        quick_sort(A, pivot+1, r)

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

A = [6,5,4,3,2,1]
quick_sort(A,0,len(A)-1)
print(A)
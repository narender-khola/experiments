class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        r = len(A)
        c = len(A[0])

        for j in range(c):
            count = 0
            for i in range(r):
                if A[i][j] == 1:
                    count+=1
                else:
                    count=0
                A[i][j] = count

        for row in A:
            row.sort(reverse=True)
        
        maxarea = 0

        for i in range(r):
            for j in range(c):
                area = A[i][j] * (j+1)
                maxarea = max(maxarea, area)
        
        return maxarea

A =[
    [1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1]
]
print Solution().solve(A)

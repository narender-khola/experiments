class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if not A:
            return 0
        r = len(A)
        c = len(A[0])
        for j in range(c):
            count = 0
            for i in range(r):
                if A[i][j] == 1:
                    count += 1
                else:
                    count = 0
                A[i][j] = count
        
        for i in range(r):
            A[i].sort(reverse=True)
                
        maxarea = -1
        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                h = A[i][j]
                w = j + 1
                maxarea = max(maxarea, h*w)
        
        return maxarea

A =[
    [1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1]
]
print Solution().solve(A)
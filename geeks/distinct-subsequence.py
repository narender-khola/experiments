class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        m = len(B)
        n = len(A)
        if n < m:
            return 0
        # print A, B
        arr = [[0 for i in range(n)] for j in range(m)]
        

        if B[0]== A[0]:
            arr[0][0]=1
        
        count = 0
        for i in range(n):
            if B[0] == A[i]:
                count+=1
            arr[0][i] = count

        for i in range(1,m):
            for j in range(1,n):
                arr[i][j] = arr[i][j-1]
                if B[i]== A[j]:
                    arr[i][j]+=arr[i-1][j-1]
        
        
        return arr[m-1][n-1]


print Solution().numDistinct('aaaababbababbaabbaaababaaabbbaaabbb','bbababa')
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        # print A, B
        if len(A)==0 or len(B)==0 or (len(B) > len(A)):
            return 0
        count = 0
        if A[0] == B[0]:
            if len(B) == 1:
                return 1 + self.numDistinct(A[1:], B[0:])
            else:
                return self.numDistinct(A[1:], B[1:]) + self.numDistinct(A[1:], B[0:])
        else:
            if len(A) == 1:
                return 0
            return self.numDistinct(A[1:], B[0:])

print Solution().numDistinct('abcd','abcd')
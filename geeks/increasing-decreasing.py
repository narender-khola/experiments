class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        B = []
        C = []
        for val in A:
            B.append(val)
            C.append(val)

        C.reverse()
        lis_1 = self.LIS(B)
        lis_2 = self.LIS(C)
        lis_2.reverse()

        maximum =0
        for i in range(len(lis_1)):
            val = lis_1[i]+ lis_2[i] -1

            # if i> 0 and lis_1[i]>lis_1[i-1] and lis_2[i]>lis_2[i-1]:
            #     val-=1
            # elif i> 0 and (lis_1[i]>lis_1[i-1] or lis_2[i]>lis_2[i-1]):
            #     val-=1
            maximum = max(val, maximum) 
        return maximum
            



    def LIS(self, A):
        lis = [1 for i in range(len(A))]
        for i in range(1,len(A)):
            max =0
            for j in range(0,i):
                if(A[j]< A[i]) and lis[j]>max:
                    max = lis[j]
            if max > 0:
                lis[i] = max + 1
        return lis

print Solution().longestSubsequenceLength([1, 11,2,10,9,8,7])
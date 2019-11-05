class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A)==1:
            return A[0]
        max1='12'
        sum1=0
        for i in A:
            if sum1+i<0:
                sum1=0
                continue
            sum1+=i
            max1=max(sum1,max1)
        if max1=='12':
            return max(A)
        else:
            return max1

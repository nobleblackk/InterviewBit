class Solution:
    # @param A : list of integers
    # @return an integer
    def count(self,A,i,j):
            Sum=abs(A[i]-A[j])+abs(i-j)
            return Sum
    def maxArr(self, A):
        res=0
        for i in range(len(A)):
            for j in range(1,len(A)):
                temp=self.count(A,i,j)
                if temp>res:
                    res=temp
        return res
        
        

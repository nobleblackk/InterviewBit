class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        i=len(A)-1
        while A[i]==9:
            A[i]=0
            i-=1
        if i>=0:
            A[i]+=1
        else:
            A.insert(0,1)
        i=0
        while True:
            if A[i]!=0:
                return A
            else:
                del A[i]
                

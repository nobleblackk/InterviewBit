class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        Sum=-1
        i=0
        ans=[]
        while i<len(A):
            while i<len(A) and A[i]<0:
                i+=1
            arr=[]
            while i<len(A) and A[i]>=0:
                arr.append(A[i])
                i+=1
            if sum(arr)>Sum:
                Sum=sum(arr)
                ans=arr
        return arr

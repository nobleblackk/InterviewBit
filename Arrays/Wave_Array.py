class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        arr=[]
        for i in range(1,len(A),2):
            arr.append(A[i])
            arr.append(A[i-1])
        if len(A)%2!=0:
            arr.append(A[len(A)-1])
        return arr

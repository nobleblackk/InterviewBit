class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        size=len(A)
        arr=[False]*size
        for i in range(size):
            if arr[A[i]]==True:
                return A[i]
            else:
                arr[A[i]]=True

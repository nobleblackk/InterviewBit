class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def check(self,x,arr,start,end):
        mid=start+(end-start)//2
        if start==end:
            if x==arr[mid]:
                return 1
            else:
                return 0
        if end>start:    
            if x==arr[mid]:
                return 1
            elif x<arr[mid]:
                return self.check(x,arr,start,mid-1)
            elif x>arr[mid]:
                return self.check(x,arr,mid+1,end)
            else:
                return 0
    def searchMatrix(self, A, B):
        n=len(A[0])-1
        for i in range(len(A)):
            if B==A[i][n]:
                return 1
            elif B<A[i][n]:
                l=self.check(B,A[i],0,n)
                if l==1:
                    return 1
                else:
                    return 0
        return 0

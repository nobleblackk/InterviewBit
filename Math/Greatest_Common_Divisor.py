"""
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3 
"""
#################################################################################################################################
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        c=1
        min=A
        if B<A:
            min=B
        for i in range(2,min+1):
            if A%i==0 and B%i==0:
                c=i
        return c

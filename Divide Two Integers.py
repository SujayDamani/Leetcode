class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        print(pow(2,31))
        if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            neg = 1
        else:
            neg = -1
        num1=bin(abs(dividend))[2:]
        num2=bin(abs(divisor))[2:]
        print(num1,num2)
        cur=''
        q=''
        for i in range(0,len(num1)):
            cur=cur+num1[i]
            if int(cur,2)<int(num2,2):
                q=q+'0'
            else:
                q=q+'1'
                cur=bin(int(cur,2)-int(num2,2))[2:]
        
            
        q=int(q,2)
        if q>(pow(2,31)-1) and neg==1:
            q=q-1
        if neg==1:
            return q
        else:
            return -q
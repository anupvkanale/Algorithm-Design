#!/usr/bin/python
import math

def mkSameLen(num1,num2):
        '''
        Given two numbers of different length, this function pads zeros
        to the smaller number and returns the numbers
        '''
        
        l1 = len(num1)
        l2 = len(num2)
        diff = abs(l1-l2)
        if(l1<l2): num1+= diff*'0'
        else: num2 += diff*'0'
        return [num1,num2,diff]

def karatsuba(num1, num2):
        '''
        Function to recursively compute the product of two numbers using the
        Karatsuba algorithm
        '''
        
        if (int(num1)<10 or int(num2)<10):
                prod = int(num1)*int(num2)
                print("single digit",num1,num2, prod)
                return prod
        else:
                [num1,num2,diff] = mkSameLen(num1,num2)
                n = len(num1)
                splitLoc = int(n/2)
                a = num1[:splitLoc]
                b = num1[splitLoc:]
                c = num2[:splitLoc]
                d = num2[splitLoc:]
                print(a,b,c,d)

                nHalf = int(n/2)
                if(n%2!=0):
                        n = n+1
                        nHalf = int(n/2)
                
                prod = pow(10,n)*karatsuba(a,c)+ pow(10,nHalf)*(
                karatsuba(a,d)+karatsuba(b,c)) + karatsuba(b,d)
                
                print("KRT",num1,num2,diff,prod)
                return prod*pow(10,-diff)

print("Karatsuba", karatsuba(str(23563),str(63445)))
print("Regular", 23563*63445)

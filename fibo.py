# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:25:07 2018

@author: Siva

Fibonacci->1,1,2,3,5,8,13
"""

if __name__=="__main__":
    pass

    
def fib2(limit):
    prev=0
    current=1
    print(str(current))
    while (prev+current)<limit:
        sum=prev+current
        print(str(sum))
        prev=current
        current=sum
        
        

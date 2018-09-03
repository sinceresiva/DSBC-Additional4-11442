# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:25:07 2018

@author: Siva

Paliandrome="Malayalam"
"""

if __name__=="__main__":
    pass
    
def ispaliandrome(inputString):
    print("Input String is {}".format(inputString))
    return inputString.lower()==inputString[::-1].lower()

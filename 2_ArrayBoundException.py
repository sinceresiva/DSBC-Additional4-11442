# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:15:37 2018

@author: Siva
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 08:20:50 2018

@author: Siva
"""
import numpy as np
def getValue(inputArray):
    try:
        index=input('Enter the index of the element to find: ')
        if(str(index).isnumeric()):
            value=inputArray[int(index)]
            print(value)
    except IndexError as ex:
        print('Array out of bound - {}'.format(ex.__class__))

inputArray=np.array([22,44,66,88,100])
getValue(inputArray)
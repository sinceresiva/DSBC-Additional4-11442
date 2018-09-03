# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 08:20:50 2018

@author: Siva
"""

def getValue(lst):
        for chr in lst:
            try:
                print('The entry is {}'.format(str(chr)))
                if(str(chr).isalpha()):
                    raise ValueError()
                elif(str(chr)=="0" or int(chr)==0):
                    raise ZeroDivisionError()
            except ValueError as ve:
                print('Oops! {} occurred.'.format(ve.__class__))
            except ZeroDivisionError as ze:
                print('Oops! {} occurred.'.format(ze.__class__))
            else:
                if(str(chr).isnumeric()):
                    print("The reciprocal of {} is {}".format(str(chr),str(1/float(chr))))
            finally:
                print('Next entry')

inputlst=['a','0',0,2,4,8]
getValue(inputlst)
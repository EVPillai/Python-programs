# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:06:40 2020

@author: siva
"""

def fib(x):
  i=1
  if x == 0 or x == 1:
      print ("x" ,x)
      return 1
  else: 
    print (x-1)
    print (x-2)
    return fib(x-1) + fib(x-2)
print(fib(4))


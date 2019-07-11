#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:10:20 2019

@author: damienrigden

This program takes an integer input from the user and returns whether or
not it is a prime. 

If not it will return the closest prime number above or below

If the input is equidistant between two primes it will return both closest primes
above and below.

"""

def isprime(x):
    if x == 1:
        return True
    
    for i in range(2, x // 2 + 1): 
        if x % i == 0:
            return False
    
    return True

def nextprime(y):
    if isprime(y):
        return y
    
    else:
        return nextprime(y + 1)

def prevprime(z):
    if isprime(z):
        return z
    
    else:
        return prevprime(z - 1)

def primequery(n):
    if isprime(n):
        
        return "{} is a prime!".format(n)
    
    else:
        if (nextprime(n) - n) < n - prevprime(n):
            return "{} is not a prime, the closest prime is {}".format(n, nextprime(n))
        
        elif nextprime(n) - n > n - prevprime(n):
            return "{} is not a prime, the closest prime is {}".format(n, prevprime(n))
        
        else:
            return "{} is not a prime, the closest primes are {} and {}".format(n, prevprime(n), nextprime(n))
        
x = int(input("Enter an integer: "))

print(primequery(x))
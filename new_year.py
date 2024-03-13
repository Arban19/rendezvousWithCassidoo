# https://twitter.com/cassidoo/status/1741732644134506696
# https://buttondown.email/cassidoo/archive/learn-from-yesterday-live-for-today-hope-for/

# Write a program that prints Happy new year! without using the string/character literals for the characters in the string!

from functools import reduce

def encode(str): # program to get the ASCII Codes
    return list(map(ord,str))

def decode(codes):
    return reduce(lambda result, code: result + chr(code), codes, "")

assert decode([72, 97, 112, 112, 121, 32, 78, 101, 119, 32, 89, 101, 97, 114, 33]) == "Happy New Year!"

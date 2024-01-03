# https://twitter.com/cassidoo/status/1741732644134506696
# https://buttondown.email/cassidoo/archive/learn-from-yesterday-live-for-today-hope-for/

# Write a program that prints Happy new year! without using the string/character literals for the characters in the string!

def encode(str): # program to get the ASCII Codes
    codes = []
    for char in str:
        codes.append(ord(char))
    return codes

def decode(codes): # main program to solve the question
    result = ""
    for code in codes:
        result += chr(code)
    return result

assert decode([72, 97, 112, 112, 121, 32, 78, 101, 119, 32, 89, 101, 97, 114, 33]) == "Happy New Year!"

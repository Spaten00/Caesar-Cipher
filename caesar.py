# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:06:44 2020

@author: Spaten
"""
import string

def caesar(word, number):
    '''
    Parameters
    ----------
    word : a string consisting of lowercase characters
    number : an integer

    Returns
    -------
    A string, in which each character of the original string is changed by 
    'number' characters of the alphabet
    '''
    letterlist = string.ascii_uppercase
    output = []
    for c in range(len(word)):
        index = letterlist.index(word[c])
        if index + number >= len(letterlist) - 1:
            output.append(letterlist[number - (len(letterlist) - index)])
        else:
            output.append(letterlist[index + number])

    return ''.join(output)

print(caesar("XYTNAUNSXPWHOTWAAHDOJKXRA",13))
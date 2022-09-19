# -*- coding: utf-8 -*-
"""
Tommy Le
CPSC 223P-01
2/3/2021
tommyle@fullerton.edu
"""

import sys

# This is my second Python program. It inspects strings.

longestWord = ""
shortestWord = ""

newString = sys.argv[1].split(" ")
longestWordLen = len(newString[1])
shortestWordLen = len(newString[1])

for word in newString:
    currentWordLen = len(word)
    if currentWordLen < shortestWordLen:
        shortestWord = word
        shortestWordLen = currentWordLen
if shortestWordLen > 1:
    print("Shortest word:", shortestWord)
    print("It is", shortestWordLen, "characters")
if shortestWordLen == 1:
    print("Shortest word:", shortestWord)
    print("It is", shortestWordLen, "character")

for word in newString:
    currentWordLen = len(word)
    if currentWordLen > longestWordLen:
        longestWord = word
        longestWordLen = currentWordLen
if longestWordLen > 1:
    print("Longest word:", longestWord)
    print("It is", longestWordLen, "characters")
if ((longestWordLen < 1) or (longestWordLen == 1)):
    print("Longest word:", longestWord)
    print("It is", longestWordLen, "character")












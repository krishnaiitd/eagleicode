#!usr/bin
import sys
import re

file = open("regex_sum_285716.txt", 'r')
data = file.read()

#print data

numData = re.findall('[0-9]+', data)

numData = [int(i) for i in numData]

print sum(numData)



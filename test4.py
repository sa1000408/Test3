import string
from math import*
import os
print pow(20,2)
print sqrt(64)
print pi
import time

print string.capwords("gis module pyth on")

path = r"D:\Pascal\SkyDrive\Masterstudium\2 Semester\14S453844 Geo Applications Standardgruppe\Exercise\Ex_01_Scripting_with_Python_I_en(2).pdf"

print os.path.dirname(path)
print os.path.basename(path)
print os.path.exists(path)
h = sqrt(169)
print h
j= (time.asctime())
# k= [time.asctime()]
# l= {time.asctime()}
strJ = j.split()

strJ = strJ[3]
print j
print strJ
strJJ = strJ.split(":")
print strJJ

# print k
# print l

# userInput = raw_input("Please enter a number")
# x = float(userInput)
#
# if x < 5:
#     print "number less than 5"
# elif x > 5:
#     print "number greater than 5"
# elif x == 5:
#     print "number = 5"
# else:
#     print "is not a number"

# fcList = ["rivers.shp", "streets.shp", "lakes.shp"]
# for x in fcList:
#     print x
for num in range (3, 7):
    print num

mixList = [1999, "January", 2003, "May", 2009, "April", "July", 2011, "January"]

for eachEntry in mixList:
    if type(eachEntry) == int:
        print eachEntry
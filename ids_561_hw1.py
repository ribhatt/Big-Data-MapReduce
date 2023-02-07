# -*- coding: utf-8 -*-
"""IDS 561 HW1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nA7P9e5rO1X0T7czsjD7kIVp1ciyGrZ
    
Riddhi Nitin Bhatt
"""

# Importing required libraries

import pandas as pd
import numpy as np
import re
import collections
import csv

#Reading the file
filename = '/temperatures.txt'
file = open(filename, 'r')
text = file.read()
file.close()

#defining a function to split the file into 2 parts
def slicefile(i):
  lines = text.split('\n')
  return lines[:500],lines[500:]

#converting to string
data1, data2 = slicefile(text)
str1 = ""
str2 = ""
for x in data1:
  str1 = str1 + "," + x

for x in data2:
  str2 = str2 + "," + x
#t1 = map(lambda x: str1 + "," + x, text1)
print(str1)
print(str2)

import re
import collections

r1 = re.findall(r"\d+, \d+", str1)

#extracting the year 
def mapper(strObj):
  strObj = strObj[0 : 4 : ] + strObj[6 : :]
  return strObj

#making a list with years and temperatures
map1 = map(mapper,r1)

list1 = list(map(lambda x : (x.split(",")[0],x.split(",")[1]), list(map1)))
print(list1)

r2 = re.findall(r"\d+, \d+", str2)

map2 = map(mapper,r2)

list2 = list(map(lambda x : (x.split(",")[0],x.split(",")[1]), list(map2)))
print(list2)

#creating dictionaries with years as keys

d1 = {}
for x,y in list1:
  if x in d1.keys():
    d1[x].append(int(y))
  else:
    d1[x] = [int(y)]
print(d1)

d2 = {}
for x,y in list2:
  if x in d2.keys():
    d2[x].append(int(y))
  else:
    d2[x] = [int(y)]
print(d2)

#Combining and sorting the data from both dictionaries

d_combine = d1.keys() | d2.keys()
d_fusion = {key: d1.get(key, []) + d2.get(key, []) for key in d_combine}

#Splitting based on years
reducer1 = {}
reducer2 = {}
reducer1_year = ['2010','2011','2012','2013','2014','2015']
reducer2_year = ['2016','2017','2018','2019','2020']

for key in d_fusion:
    if key in reducer1_year:
        reducer1[key] = d_fusion[key]
    else:
        reducer2[key] = d_fusion[key]

print(reducer1)
print(reducer2)

#Finding the maximum values in reducer 1 and reducer 2

reducer1_maxval = {}
for key in reducer1:
    maxval = max(reducer1[key])
    reducer1_maxval[key] = maxval

print(reducer1_maxval)


reducer2_maxval = {}
for key in reducer2:
  maxval = max(reducer2[key])
  reducer2_maxval[key] = maxval

print(reducer2_maxval)

#merge the dictionaries and write it to the output file 
results = {**reducer1_maxval, **reducer2_maxval}

import csv
dict = results
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Year', 'Max Value'])
    for key in dict.keys():
        writer.writerow([key, dict[key]])

"""## Since we can condense all the above processes in a single function. We will do that in the next section"""

import re
import csv

def process_file(filename):
  with open(filename, 'r') as file:
    text = file.read()
    
  lines = text.split('\n')
  data1 = lines[:500]
  data2 = lines[500:]

  str1 = ",".join(data1)
  str2 = ",".join(data2)

  r1 = re.findall(r"\d+, \d+", str1)
  r2 = re.findall(r"\d+, \d+", str2)

  def mapper(str_obj):
    return str_obj[0:4] + str_obj[6:]
  
  map1 = map(mapper, r1)
  list1 = list(map(lambda x: (x.split(",")[0], x.split(",")[1]), list(map1)))

  map2 = map(mapper, r2)
  list2 = list(map(lambda x: (x.split(",")[0], x.split(",")[1]), list(map2)))

  d1 = {}
  for x, y in list1:
    if x in d1.keys():
      d1[x].append(int(y))
    else:
      d1[x] = [int(y)]

  d2 = {}
  for x, y in list2:
    if x in d2.keys():
      d2[x].append(int(y))
    else:
      d2[x] = [int(y)]

  d_combine = set(d1.keys()) | set(d2.keys())
  d_fusion = {key: d1.get(key, []) + d2.get(key, []) for key in d_combine}

  reducer1_year = ['2010', '2011', '2012', '2013', '2014', '2015']
  reducer2_year = ['2016', '2017', '2018', '2019', '2020']

  reducer1 = {key: d_fusion[key] for key in d_fusion if key in reducer1_year}
  reducer2 = {key: d_fusion[key] for key in d_fusion if key in reducer2_year}

  reducer1_maxval = {key: max(reducer1[key]) for key in reducer1}
  reducer2_maxval = {key: max(reducer2[key]) for key in reducer2}

  results = {**reducer1_maxval, **reducer2_maxval}

  with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Year', 'Max Value'])
    for key in results.keys():
      writer.writerow([key, results[key]])

process_file('/temperatures.txt')


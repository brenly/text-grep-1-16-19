import fnmatch
import os
import glob
import re

#this a simple grep script to pull a database from a text file. future versions will include sql.

for filename in glob.glob('*.txt'):
  with open(filename, 'r') as f:
    for line in f:
      if line[1:4].isdigit() and line[6:10].isdigit():
        print("-----------------------")
        print (line[1:4]) #branch
        print (line[6:10]) #emplid
        print (line[11:42]) #empl name
        print (line[42:52]) #pin
        print (line[53:67]) #home number
        print (line[69:83]) #work cell
        print (line[84:86]) #cc?
        print (line[94:97]) #svc digit?
        print (line[98:128])
        if len(line) > 129:
          print (line[129:159])
      elif line[0:42].isspace() and re.search('[\w]', line[98:128]): #elif detects multi line comments
          print (line[98:128])
          if len(line) > 129:
            print (line[129:159])

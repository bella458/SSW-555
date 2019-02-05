"""Bella Manoim Project 2
   Purpose: Practice programming with GEDCOM data
"""

import re

"""Validate and open file"""
try:
    """filename = open('project1_BellaManoim.ged')""" #Comment out the file not being read
    filename = open('proj02test.ged') #This is the provided sample file
except FileNotFoundError:
    print ('File cannot be opened.')
    exit()


validtags = {'INDI':[0,[]],'NAME':[1,['INDI']],'SEX':[1,['INDI']],'BIRT':[1,['INDI']],
'DEAT':[1,['INDI']],'FAMC':[1,['INDI']],'FAMS':[1,['INDI']],'FAM':[0,[]],'MARR':[1,['FAM']],
'HUSB':[1,['FAM']], 'WIFE':[1,['FAM']],'CHIL':[1,['FAM']],'DIV':[1,['FAM']],
'DATE':[2,['BIRT','DEAT','DIV','MARR']], 'HEAD':[0,[]],'TRLR':[0,[]],'NOTE':[0,[]]}

"""Cleaning up the arguments back into string"""
def cleanArguments(list):
    newstring = ""
    for word in list:
        if switched == True:
            newstring = newstring + word
        else:
            newstring = newstring + ' ' + word
    return newstring

"""Check if tag and level match a pair in the dictionary"""
def validTagsCheck(level,tag):
    if tag not in validtags:
        return "N"
    if validtags[tag][0] == level:
        return "Y"
    else:
        return "N"

isValid = ""
"""Go through each line in file, determine if tag is valid and if level is valid"""
for line in filename:
    line = line.strip() #remove whitespace, including new lines
    level = int(line[0])
    splitline = line.split()
    switched = False

    if len(splitline) <= 2:
        tag = splitline[1]
        arguments = ''
        isValid = validTagsCheck(level,tag)
    elif len(splitline) > 2:
        if splitline[2] in validtags:
            tag = splitline[2]
            arguments = splitline[1]
            isValid = validTagsCheck(level,tag)
            switched = True
        elif splitline[1] in validtags:
            tag = splitline[1]
            arguments = splitline[2:]
            isValid = validTagsCheck(level,tag)
        else:
            isValid = "N"
            tag = splitline[1]
            arguments = splitline[2:]
        if level == 0 and splitline[1] == 'FAM' or splitline[1] == 'INDI':
            tag = splitline[1]
            arguments = splitline[2:]
            isValid = "N"

    arguments = cleanArguments(arguments)
    print("-->", line)
    print("<--", level, "|", tag, "|", isValid, "|", arguments)
    print() #print blank line between each couple

#!/usr/bin/python
import sys
import csv
import re
import getopt
import fileinput
import json

fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]
unixOptions = "f:"
defaultCol = 1
nameFileDir ='data/Homo_sapiens.GRCh37.75.gtf'
testFileDir =''
lookupGeneID={}

try:
    arguments, values = getopt.getopt(argumentList, unixOptions)
except getopt.error as err:
    print (str(err))
    sys.exit(2)
for currentArgument, currentValue in arguments:
    if (currentArgument in ("-f") and len(argumentList) == 2):
        defaultCol = int(currentValue)
if (len(argumentList) == 1):
    testFileDir = sys.argv[1]
else:
    testFileDir = sys.argv[2]

for line in fileinput.input(nameFileDir):
    if re.match(r'.*\t.*\tgene\t', line):
        gene_id_matches = re.findall('gene_id \"(.*?)\";', line)
        gene_name_matches = re.findall('gene_name \"(.*?)\";', line)
        if gene_id_matches and gene_name_matches:
            lookupGeneID[gene_id_matches[0]] = gene_name_matches[0]

for line in fileinput.input(testFileDir):
    textList = re.split(',',line.rstrip())
    idInTest = re.findall(r'[a-zA-Z]+\d+', textList[defaultCol-1])
    if idInTest:
        for id in idInTest:
            if id in lookupGeneID:
                print textList[0] + "," + lookupGeneID[id] + "," + textList[2] + "," + textList[3] + "," + textList[4]

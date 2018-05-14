# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 14:08:31 2017

@author: Mahdix
"""
import csv
def retrieve_Hsheet(filename):
    infile = open(filename,'r')
    csvdata =csv.reader(infile)
    Hsheet=[]
    for row in csvdata:
        Hsheet.append(row)
    infile.close()
    return Hsheet
def wanted_cols_func(filename,except_cols):
    infile = open(filename,'r')
    csvdata =csv.reader(infile)
    wanted_cols=[]
    for row in csvdata:
        if row[0] not in except_cols:
                wanted_cols.append(row[0])
    infile.close()
    return wanted_cols

def retrieve_axis(filename):
    infile = open(filename,'r')
    csvdata =csv.reader(infile)
    wanted_cols=[]
    for row in csvdata:
        wanted_cols.append(row[1])
    infile.close()
    return wanted_cols

def retrieve_cols(filename,cols,wanted_cols):
    infile = open(filename,'r')
    csvdata =csv.reader(infile)
    for row in csvdata:
        if row[0] == cols and row[2]==wanted_cols:
            result=_intStrArray(row[3:])
    infile.close()
    return result
def retrieve_col(filename,wanted_col):
    infile = open(filename,'r')
    csvdata =csv.reader(infile)
    for row in csvdata:
        if row[0] == wanted_col:
            result=_intStrArray(row[1:])
    infile.close()
    return result
def _intStrArray(row):
    for ii in range(len(row)):
        if row[ii]=='':
            row[ii]='0'
    return row
    
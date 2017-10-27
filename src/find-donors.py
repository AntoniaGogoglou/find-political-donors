#!/usr/bin/python

import csv
import os
import sys
from collections import OrderedDict
import math

#args contains the input file path and output files path
def main(args):
    d=OrderedDict()
    dd=OrderedDict()
    inputFile=args[1]
    with open(inputFile,'rb+') as f:
        reader=csv.reader(f)
        for line in reader:
            # ReqFields contains the required fields extracted from each line
            ReqFields, flag=stream_Line_to_Fields(line)
            ##if line valid and zip valid
            if flag==1 and (ReqFields[1] is not '00000'):
                CMTE_ZIP=(ReqFields[0],ReqFields[1])
                d=update_Dict(d,ReqFields,CMTE_ZIP)
                currMedian=median(d[CMTE_ZIP][2])
                with open(args[2]+'/medianvals_by_zip.txt',"a+") as ff:
                    ff.write("%s|" % CMTE_ZIP[0])
                    ff.write("%s|" % CMTE_ZIP[1])
                    ff.write("%s|" % str(currMedian))
                    ff.write("%s|" % str(d[CMTE_ZIP][1]))
                    ff.write("%s" % str(d[CMTE_ZIP][0]))
                    ff.write("\n")
                ff.close()
            ##if line valid and DT valid
            if flag==1 and (ReqFields[2] is not '00000000'):
                CMTE_DT=(ReqFields[0],ReqFields[2])
                dd=update_Dict(dd,ReqFields,CMTE_DT)
    f.close() 
    # sort output for medianvals_by_date file
    ddSorted=OrderedDict(sorted(dd.items(), key=lambda key: key[0:1])) 
    with open(args[2]+'/medianvals_by_date.txt',"a+") as ff:
        for rec_DT in ddSorted:
            ff.write("%s|" % rec_DT[0])
            ff.write("%s|" % rec_DT[1])
            ff.write("%s|" % str(median(ddSorted[rec_DT][2])))
            ff.write("%s|" % str(ddSorted[rec_DT][1]))
            ff.write("%s" % str(ddSorted[rec_DT][0])) 
            ff.write("\n")
    ff.close()
    
## ID, ZIP and DT are strings, the rest are int
def stream_Line_to_Fields(line):
    lineAsStr=" ".join(line)
    fields = lineAsStr.split('|')
    ## flag=0 means do not contemplate line
    flag=0
    ReqFields=[]
    #check for OTHER_ID
    if not fields[15]:
        # check for missing CMTE_ID and TRANSACTION_AMT
        if fields[0] and fields[14]:
            # if there is date, check that it is valid
            if fields[13]:
                month=fields[13][:2]
                day=fields[13][2:4]
                year=fields[13][4:]
            if not fields[13] or int(month)>12 or int(month)<1 or int(day)>31 or int(day)<1 or int(year)>2018 or int(year)<1900:
                fields[13]='00000000'
            # check for invalid zip
            if not fields[10] or len(fields[10])<5:
                fields[10]='00000'
            ReqFields=[fields[0],fields[10][0:5],fields[13],int(fields[14])]
            flag=1
    return ReqFields, flag

def update_Dict(d,ReqFields,tuple_key):
    if tuple_key not in d:
        count=1
        d[tuple_key]=[int(ReqFields[3]),count,[int(ReqFields[3])]]
    else:
        d[tuple_key][0]=d[tuple_key][0]+int(ReqFields[3])
        d[tuple_key][1]=d[tuple_key][1]+1
        d[tuple_key][2].append(int(ReqFields[3]))
    return d
    
def median(l):
    ##Calculate median of the given list.
    sortL = sorted(l)
    half, odd = divmod(len(sortL), 2)
    if odd:
        return sortL[half]
    return int(math.ceil((sortL[half - 1] + sortL[half]) / 2.0))

##when using this then the list in the dictionary will be updated sorted!
##better space complexity because the list is sorted in place (use in case of bigger datasets)
def medianInPlace(l):
    ##Calculate median of the given list.
    l.sort()
    half, odd = divmod(len(l), 2)
    if odd:
        return l[half]
    return int(math.ceil(l[half - 1] + l[half] / 2.0))


if __name__ == "__main__": 
    main(sys.argv)

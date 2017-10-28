# find-political-donors

This repo contains the script for identifying donations to election campaings per date and zip code. In the ./input folder, you can find a sample input itcont.txt of donations, while in the ./output folder the outputs are stored for zip codes and dates.

The code is contained withing the script ./src/find-donors.py and is run using the commands found in ./run.sh. 
There are no "exotic" dependencies for the script to run, just the following module imports:
* import csv
* import os
* import sys
* from collections import OrderedDict
* import math

The proces followed can be summed up in the following steps:
* Read input file
* For each line select only the required fields
  * create two python dictionaries: d and dd
    * d has as key the tuple of 'CMTE_ID' and 'ZIP', while value is a list containing the summation of TRANSACTION_AMT, a count of the number
      of contributions and finally a list of each TRANSACTION_AMT so far
    * dd has as key the tuple of 'CMTE_ID' and 'TRANSACTION_DT', while value is a list contaiing the containing the summation of TRANSACTION_AMT, a count of the number of contributions and finally a list of each TRANSACTION_AMT so far
  * check if values are valid 
  * write a new line to the file medianvals_by_zip.txt containing the median value of transactions so far, number and total amount of contributions for each CMTE_ID and ZIP combination
* Aggregating over all lines, write to the file medianvals_by_date.txt containing the median value of transactions so far, number and total amount of contributions for each CMTE_ID and TRANSACTION_DT combination

Helper functions include a function to get the required fields from each line (stream_Line_to_Fields), one to update the dictionary values when a new line is added (update_Dict) and finally a function to calculate the median of a list (median/medianInPlace). 

NOTE: there are two median functions in find-donors.py, one called 'median' and another one called 'medianInPlace'. Both calculate the median of a list but use different methods to sort the list, 'medianInPlace' uses 'sort' instead of 'sorted', which means that the list is sorted in place leading to better space complexity for larger datasets. In our epxeriments we used the classic 'median' since performance was good enough even with larger datasets downloaded from FEC (http://classic.fec.gov/finance/disclosure/ftpdet.shtml#a2017_2018)

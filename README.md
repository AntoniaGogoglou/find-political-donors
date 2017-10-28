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

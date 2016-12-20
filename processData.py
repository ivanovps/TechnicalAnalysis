# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 15:03:42 2016

@author: paivanov
"""

import csv as csv 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import glob, os

os.chdir("ReadData")
#for file in xrange(3): #glob.glob("*.csv"):
files = glob.glob("*.csv");
for i in xrange(1):
    csvObject = csv.reader(open(files[i]));
    csvObject.next(); # read first line, which is header
    quoteData = [];
    for row in csvObject:
        quoteData.append(row)
        
    quoteData = np.array(quoteData);
    quoteData = quoteData[0::,1:6]
    quoteData = quoteData.astype(np.float)
    plt.figure();
    plt.plot(quoteData[0::,3])
    #plt.title(files[i])


        

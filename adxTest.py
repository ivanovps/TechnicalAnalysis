# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:38:13 2016

@author: paivanov
"""

import csv as csv 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from adxfunction import adxfunction

csvObject = csv.reader(open("adxTest.csv"));
quoteData = [];
for row in csvObject:
    quoteData.append(row)

    
quoteData = np.array(quoteData);
quoteData = quoteData[0::,1:4];
quoteData = quoteData.astype(np.float)
DM1Plus, DM1Minus, tr, DM14Plus, DM14Minus, DIPlus, DIMinus, dx, adx = adxfunction(quoteData, 14)
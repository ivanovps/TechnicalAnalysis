# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 15:03:42 2016

@author: paivanov
"""

import csv as csv 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from indicators import movingAverage, exponentialMovingAverage, movingAverageConvergenceDivergence
from profit import profit
from orders import orders
from adx import adx

import glob, os

csvObject = csv.reader(open("ReadData\AAPL.csv"));
csvObject.next(); # read first line, which is header
quoteData = [];
for row in csvObject:
    quoteData.append(row)
        
quoteData = np.array(quoteData);
quoteData = quoteData[0::,1:6]
quoteData = quoteData.astype(np.float)
price = quoteData[1000::,3];

plt.figure();
plt.plot(price)
plt.plot(movingAverage(price,200));
plt.plot(exponentialMovingAverage(price,200, 0.1));

plt.figure()
(macd, signal) = movingAverageConvergenceDivergence(price, 24, 52, 9, 0.1 )
plt.plot(macd)
plt.plot(signal)

(buyOrders, sellOrders) = orders(macd, signal)
(profitability, investmentValue) = profit(buyOrders, sellOrders, price)
print profitability

plt.figure();
plt.plot(investmentValue)

adx(quoteData, 14)

        

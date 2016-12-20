# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 21:00:04 2016

@author: paivanov
"""

import numpy as np

def profit(buyOrders, sellOrders, price):
    # initialie cash and share amounts
    initialValue = 100;
    cache = initialValue;
    shares = 0;
    investmentValue = np.zeros(len(price))
    # determine index of first buy order
    firstBuyOrder = np.where(buyOrders)[0][0];

    # go through time line and execute sell and buy orders 
    for i in xrange(firstBuyOrder, len(price)):
        if buyOrders[i]==1:
            shares = cache/price[i]
            cache = 0
        if sellOrders[i]==1:
            cache = shares*price[i]
            shares = 0;
        investmentValue[i] = cache + shares*price[i]
    # calculate final value of investment
    finalValue = cache + shares*price[-1]
    profitability = finalValue/initialValue
    return (profitability, investmentValue)
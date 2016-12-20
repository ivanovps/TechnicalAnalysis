# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 21:34:05 2016

@author: paivanov
"""

import numpy as np

def orders(macd, signal):
    buySignals = macd-signal
    buySignals = buySignals>0.01
    sellSignals = macd-signal
    sellSignals = sellSignals<0.01
    inCache = 1;
    buyOrders = np.zeros(len(macd))
    sellOrders = np.zeros(len(macd))
    for i in xrange(len(macd)):
        if (buySignals[i] & inCache):
            buyOrders[i] = 1
            inCache = 0
        if (sellSignals[i] & ~inCache):
            sellOrders[i] = 1
            inCache = 1
            
    return (buyOrders, sellOrders)
        
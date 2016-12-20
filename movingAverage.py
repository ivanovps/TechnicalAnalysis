# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:00:47 2016

@author: paivanov
"""

# unction calculates moving average
# x is the 1D array
# w is the width of a moving window

import numpy as np;

def movingAverage(x, w):
    x = np.asarray(x);
    y = np.zeros(len(x));
    for i in xrange(len(x)):
        start = max(0,i-w+1);
        y[i] = np.mean(x[start:i]);
    return y
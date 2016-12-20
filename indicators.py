# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:00:47 2016

@author: paivanov
"""

# unction calculates moving average
# x is the 1D array
# w is the width of a moving window

import numpy as np;

def movingAverageConvergenceDivergence(x, shortw, longw, signalw, alpha ):
    macd_ = exponentialMovingAverage(x, shortw, alpha) - exponentialMovingAverage(x, longw, alpha)
    signal = exponentialMovingAverage(macd_, signalw, alpha)
    return (macd_, signal)

def exponentialMovingAverage(x, window, alpha):
    x = np.asarray(x);
    y = np.zeros(len(x));

    for i in xrange(len(x)):
        start = max(0,i-window+1);
        y[i] = x[start];
        for j in xrange(start,i):
            y[i] = alpha*x[j] + (1-alpha)*y[i];
    return y

def movingAverage(x, w):
    x = np.asarray(x);
    y = np.zeros(len(x));
    for i in xrange(len(x)):
        start = max(0,i-w+1);
        y[i] = np.mean(x[start:i]);
    return y
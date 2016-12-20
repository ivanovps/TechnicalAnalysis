# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:02:19 2016

@author: paivanov
"""
# ADX algorithm reference:http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_directional_index_adx

import numpy as np;

def adxfunction(data, w):
    high = data[0::,0];
    low = data[0::,1];
    
    # window (is defined by the author to be 14)
    w = 14;
    
    N = len(high); # N is the length of the chart
    
    DM1Plus = np.zeros(N);
    DM1Minus = np.zeros(N);
    tr = np.zeros(N);

    # direction movements
    DM14Plus = np.zeros(N);
    DM14Minus = np.zeros(N);
    tr14 = np.zeros(N);

    # directional indicators
    DIPlus = np.zeros(N);
    DIMinus = np.zeros(N);

    # direction index
    dx = np.zeros(N);

    # average directional index
    adx = np.zeros(N);

    # compute directional movements
    for i in xrange(1, N): 
        DM1Plus[i] = max(high[i]-high[i-1],0);
        DM1Minus[i] = max(low[i-1]-low[i],0);
        tr[i] = high[i]-low[i];

    #compute directional indicators
    # initialize 14th element to the sums of the first 14 elements
    DM14Plus[w-1] = sum(DM1Plus[0:w-1]);
    DM14Minus[w-1] = sum(DM1Minus[0:w-1]);
    tr14[w-1] = sum(tr[0:w-1]);
    for i in xrange(w,N):
        DM14Plus[i] = DM14Plus[i-1]-(DM14Plus[i-1]/w)+DM1Plus[i];
        DM14Minus[i] = DM14Minus[i-1]-(DM14Minus[i-1]/w)+DM1Minus[i];
        tr14[i] = tr14[i-1]-(tr14[i-1]/w)+tr14[i];
        # compute directional indexes
        DIPlus[i] = DM14Plus[i]/tr14[i]*100; # multiply by 100 (lind of normalization)
        DIMinus[i] = DM14Minus[i]/tr14[i]*100;

        # compute directional movement index
        dx[i] = DIPlus[i] - DIMinus[i]

    # smooth dx
    adx[2*w-1] = sum(dx[w-1:2*w-2]);
    for i in xrange(w,N):
        adx[i] = (adx[i-1]*(w-1)+dx[i])/w
        
    return (DM1Plus, DM1Minus, tr, DM14Plus, DM14Minus, DIPlus, DIMinus, dx, adx)
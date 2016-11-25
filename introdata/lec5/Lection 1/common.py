# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", module="matplotlib")

FONT = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 10}


def plot_drv(name, values, cdf, pmf):
    fig, ax = plt.subplots(2, sharex=True, figsize = (10,5))
    plt.title(name)
    cdf_name = ' '.join((name, 'cdf'))
    ax[0].plot(values, cdf, 'bo', ms=6, label=cdf_name)
    #ax[0].vlines(values, 0, cdf, colors='b', lw=3, alpha=0.3)
    ax[0].set_xlim([min(values)-0.1,max(values)+0.1])
    ax[0].set_ylim([0, max(cdf) + 0.05])
    ax[0].set_ylabel('F(x)', fontsize=14, weight='bold', color='blue')
    ax[0].hlines(cdf[:np.size(cdf)-1], values[:np.size(values)-1], values[1:], "b")
    plt.xlabel('x', fontsize=14, weight='bold', color='blue')
    #plt.ylabel('F(x)', fontsize=14, weight='bold')
    
    pmf_name = ' '.join((name, 'pmf'))
    ax[1].plot(values, pmf, 'bo', ms=6, label=pmf_name)
    ax[1].vlines(values, 0, pmf, colors='b', lw=3, alpha=0.3)
    ax[0].set_xlim([min(values)-0.1,max(values)+0.1])
    ax[1].set_ylim([0,max(pmf) + 0.02])
    ax[1].set_ylabel('p(x)', fontsize=14, weight='bold', color='blue')
    plt.rc('font', **FONT)

def plot_crv(name, values, cdf, pmf, set_ylim=False):
    fig, ax = plt.subplots(2, sharex=True, figsize = (5,10))
    plt.title(name)
    cdf_name = ' '.join((name, 'cdf'))
    ax[0].plot(values, cdf, 'r-', lw=5, alpha=0.6, label=cdf_name)
    #ax[0].set_xlim([min(values),max(values)])
    ax[0].set_ylim([0, max(cdf) + 0.05])
    ax[0].set_ylabel('F(x)', fontsize=14, weight='bold', color='blue')

    plt.xlabel('x', fontsize=14, weight='bold', color='blue')
    #plt.ylabel('F(x)', fontsize=14, weight='bold')
    
    pmf_name = ' '.join((name, 'pmf'))
    ax[1].plot(values, pmf, 'r-', lw=5, alpha=0.6, label=pmf_name)
    #ax[0].set_xlim([min(values),max(values)])
    if set_ylim:
        ax[1].set_ylim([0,max(pmf) + 0.02])
    ax[1].set_ylabel('f(x)', fontsize=14, weight='bold', color='blue')
    plt.rc('font', **FONT)
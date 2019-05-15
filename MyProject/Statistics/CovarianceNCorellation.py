# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import mean
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson
import scipy.stats as sp


def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y))

pageSpeeds = np.random.normal(3, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

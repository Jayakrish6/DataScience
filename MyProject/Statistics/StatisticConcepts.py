# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson
import scipy.stats as sp

incomes = np.random.normal(27000, 15000, 100000)
#np.mean(incomes)

#plt.hist(incomes, 50)
#plt.show()

print(np.median(incomes))

plt.hist(incomes, 50)
plt.show()

ages = np.random.randint(18, high=90, size=500)
#print(ages)

stats.mode(ages)
plt.hist(ages, 50)
plt.show()

incomes = np.random.normal(100.0, 20.0, 10000)

plt.hist(incomes, 50)
plt.show()

print(incomes.std())
print(incomes.var() )

#Uniform distribution
values = np.random.uniform(-10.0, 10.0, 10000)
plt.hist(values, 50)
plt.show()

#Normal or Gaussian distribution
x = np.arange(-3, 3, 0.001)
plt.plot(x, norm.pdf(x))

mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.show()

#Expontial PDF(Probability Distribution Function)/"Power Law"
x = np.arange(0, 10, 10000)
plt.plot(x, expon.pdf(x))
#Binomial probability mass function
n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))

#Poisson probability mass function
mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))

vals = np.random.normal(0, 0.5, 10000)
plt.hist(vals, 50)
plt.show()

print(np.mean(vals))
print(np.var(vals))
print(sp.skew(vals))
print(sp.kurtosis(vals))

plt.hist(vals, 50)
plt.show()

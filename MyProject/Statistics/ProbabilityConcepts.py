# -*- coding: utf-8 -*-
from numpy import random
random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0

for _ in range (10000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = float(ageDecade)/100.0
    totals[ageDecade] += 1
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        totals[ageDecade] += 1

print(totals)
print(purchases)
print(totalPurchases)

PEF = float(purchases[30]) / float(totals[30])
print("P(purchase | 30s)", PEF)

PE = float(totalPurchases) / 10000.0
print("P(purchase)", PE)



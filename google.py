import random
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Each trial has 100 couple who gives births like it is stated in the question. 
# Then, the ratio of boys and girls is calculated for that trial.

t = int(input("Number of trials : "))

valdata = []
ratiodata = []

avg = 0

for a in range(0, t):
    b = 0 
    g = 0
    for i in range(0,100):
        initial = g
        n = random.random()
        if n < 0.50: 
            b += 1
        while n >= 0.50:
            g += 1
            n = random.random()
            if n < 0.50:
                b += 1
                val = g-initial
                valdata.append(val)
    avg = avg + g/b
    ratiodata.append(g/b)
print()
print('Average son to daughter ratio \t =', avg/t)
df = pd.DataFrame(ratiodata, columns = ['Ratio'])
dval = pd.DataFrame(valdata, columns = ['Number of daughters before having the first son'])


q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
iqr = q3 - q1
bin_width = (2 * iqr) / (len(df) ** (1 / 3))
bin_count = int(np.ceil((df.max() - df.min()) / bin_width))


f, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 6))
sb.histplot(df, bins = bin_count, kde = True, ax=axes)

f, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 6))
sb.histplot(dval, kde = False, ax=axes)

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy import stats

nResamp = 100000
smurfs = [13.6, 10.3, 10.0, 16.0, 12.4, 9.1, 14.5, 10.2,
        8.9, 11.1, 15.9, 9.5, 10.4]
dwarfs = [11.0, 8.9, 8.0, 14.0, 11.4, 8.1, 28.5]

print np.mean(smurfs), np.mean(dwarfs) # these are height-units difference in mean height of dwarfs and smurfs
origDiff = np.mean(smurfs) - np.mean(dwarfs)

popN = smurfs + dwarfs

allDiffs = []
for n in range(nResamp):
    random.shuffle(popN) # shuffle in place
    
    reSampDwarfs = popN[:len(dwarfs)] # resample our dwarf population; m
    reSampSmurfs = popN[len(dwarfs):] # assume the rest of the sample are smurfs
    reSampDiff = np.mean(reSampSmurfs) - np.mean(reSampDwarfs)
    allDiffs.append(reSampDiff)

plt.hist(allDiffs) # plot a histogram of the distribution under the null hypothesis; more accurate than real NH?
#plt.show()

allDiffs.sort() # sort in place
bottomCrit = allDiffs[int(0.025*nResamp)] # bottom criterion value that must be exceeded
topCrit = allDiffs[int(0.975*nResamp)] # top criterion value that must be exceeded
print bottomCrit,topCrit
print stats.percentileofscore(allDiffs, origDiff) # show percentage likelihood (i.e. p-value) of seeing these distributions under the null hypothesis


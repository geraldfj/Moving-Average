import numpy as np

dataset = [1,5,7,2,6,7,8,2,5,2,6,8,2,6,13]

def movingaverage(values,window):
    weights = np.repeat(1.0,window)/window
    smas = np.convolve(values,weights,'valid')
    return smas

print(movingaverage(dataset,3))

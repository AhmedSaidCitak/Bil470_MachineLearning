import numpy as np

train = open('train1.csv', 'w')
validation = open('val1.csv', 'w')

with open('train.csv', 'r') as f:
    for line in f:
        randomNumber = np.random.random(1)[0]
        f.readline()
        if(randomNumber > 0.2):
            train.write(line)
        else:
            validation.write(line)
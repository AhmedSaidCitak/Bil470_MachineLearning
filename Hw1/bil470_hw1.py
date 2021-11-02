import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def test(accuracy):
    with open('val1.csv', 'r') as f:
        count = 0
        correct = 0
        f.readline()
        for line in f:

            predictors = line.split(',')
            target = predictors[-1]
            target = target.replace("\n", "")
            target = float(target)
            predictors = np.asarray(predictors[1:-1], dtype=float)

            res = np.dot(betas[1:], predictors.T)
            sum = np.sum(res)

            z = betas[0] + sum

            modelout = sigmoid(z)
            if(modelout > 0.5 and target == 1):
                correct += 1
            if (modelout <= 0.5 and target == 0):
                correct += 1
            count += 1
        accuracy.append(1.0 * correct/count)

betas = np.random.normal(0,0.1,286)
target = []

with open('train1.csv', 'r') as f:
    accuracy = []
    f.readline()
    count = 0
    for line in f:
        if (count % 20000 == 0):
            test(accuracy)
        count += 1
        tempPredictors = line.split(',')
        tempTarget = tempPredictors[-1]
        tempTarget = tempTarget.replace("\n", "")
        tempTarget = float(tempTarget)
        tempPredictors = np.asarray(tempPredictors[1:-1], dtype=float)

        res = np.dot(betas[1:], tempPredictors.T)
        sum = np.sum(res)

        z = betas[0] + sum

        betas[0] += 0.00005 * (tempTarget - sigmoid(z))
        for i in range (1,286):
            betas[i] += 0.00005 * (tempTarget - sigmoid(z)) * tempPredictors[i-1]

    epoch = list(range(0, len(accuracy)))
    plt.plot(epoch, accuracy)
    plt.show()
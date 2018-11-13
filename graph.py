import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error, r2_score

f = open("gammas.out", "r")
arr = []
arr_full = []
for line in f:
    k = line.split(" ")
    if (int(k[0]) > 1000):
        arr.append(float(k[1]))
    arr_full.append(float(k[1]))
arr2 = np.array(arr)
arr_full = np.reshape(np.array(arr_full), (-1, 1))
print(len(arr_full))
arr3 = []
idxs = []
idx_full = []

full_features = []
for i in range(1001, 2001):
    arr3.append(math.sqrt(i*math.log(i)))

for i in range(1, 2001):
    full_features.append(math.sqrt(i*math.log(i)))
    idx_full.append(i)
full_features = np.reshape(np.array(full_features), (-1, 1))
arr4 = np.array(arr3)
regr = linear_model.LinearRegression()
arr4 = np.reshape(arr4, (-1, 1))
arr2 = np.reshape(arr2, (-1, 1))
arr3 = np.reshape(arr3, (-1, 1))
regr.fit(arr4, arr2);
y_pred = regr.predict(full_features);
print(regr.coef_)
print(len(y_pred))
print(arr_full)
print(y_pred)
#plt.plot(idx_full, arr_full - y_pred, color = 'black', linewidth = 3) #display error
plt.plot(idx_full, arr_full, color = 'black', linewidth = 1.5) #display simulated values
plt.plot(idx_full, y_pred, color = 'blue', linewidth = 1.5) #display predicted values
plt.xticks()
plt.yticks()
#plt.savefig('error5Mtrials.png')
#plt.savefig('simvalues.png')
#plt.savefig('predvalues.png')
plt.savefig('combvalues.png')

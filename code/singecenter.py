import json
import re
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from sklearn import datasets
from sklearn import metrics
from sklearn.cluster import KMeans

def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

center = np.array([[-37.815018057437975,144.9681330478775]])


#color = ['black','red','blue','yellow']
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'
x,y = np.loadtxt('./total_17_city.txt', delimiter=',', unpack=True)


plt.figure(figsize=(20,20))
plt.scatter(center[:,1],center[:,0],marker='+',c='k', zorder = 20, label='center')
plt.title('Melbourne City Alcohol Distribution')
plt.plot(y, x, '.', label='Data', color='r',zorder = 10)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()










import json
import re
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from sklearn import datasets
from sklearn.cluster import DBSCAN

#color = ['black','red','blue','yellow']
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'
x,y = np.loadtxt('./total_17_city.txt', delimiter=',', unpack=True)
list = []
for index,value in enumerate(x):
    tmpx = x[index]
    tmpy = y[index]
    tmp =[tmpx,tmpy]
    list.append(tmp)
raw = np.array(list)

sumx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sumy = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
centerx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
centery = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#1
#result = DBSCAN(eps=0.03,min_samples=1000).fit_predict(raw)
#2
result = DBSCAN(eps=0.01,min_samples=600).fit_predict(raw)
#3
#result = DBSCAN(eps=0.01,min_samples=700).fit_predict(raw)

for index,c in enumerate(result):
    if c >= 0:
        sumx[c] += raw[:,0][index]
        sumy[c] += raw[:,1][index]
        num[c] += 1
cenlist = []
for i in range(14):
    if num[i] >0:
        centerx[i] = sumx[i]/num[i]
        centery[i] = sumy[i]/num[i]
        cenlist.append([centerx[i],centery[i]])
center = np.array(cenlist)
for i in center:
    print(i)
plt.figure(figsize=(9,9))
plt.scatter(raw[:,1],raw[:,0],c=result,marker='.',zorder=10)
plt.scatter(center[:,1],center[:,0],c='k',marker='+',zorder=20,s=100)
plt.show()

#plt.plot(y, x, '.', label='Data', color='b')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Data')
#plt.legend()
#plt.show()










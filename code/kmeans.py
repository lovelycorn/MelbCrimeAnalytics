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


#color = ['black','red','blue','yellow']
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'
x,y = np.loadtxt('./total_17_city.txt', delimiter=',', unpack=True)
print(type(x))

list = []
for index,value in enumerate(x):
    tmpx = x[index]
    tmpy = y[index]
    tmp =[tmpx,tmpy]
    list.append(tmp)
#print(list)
raw = np.array(list)
result = KMeans(n_clusters=7).fit_predict(raw)

cen0x = []
cen0y = []
cen1x = []
cen1y = []
cen2x = []
cen2y = []
cen3x = []
cen3y = []
cen4x = []
cen4y = []
cen5x = []
cen5y = []
cen6x = []
cen6y = []
for index,value in enumerate(result):
    tmpx = x[index]
    tmpy = y[index]
    tmpc = result[index]
    if int(tmpc) == 0:
        cen0x.append(float(tmpx))
        cen0y.append(float(tmpy))
    if int(tmpc) == 1:
        cen1x.append(float(tmpx))
        cen1y.append(float(tmpy))
    if int(tmpc) == 2:
        cen2x.append(float(tmpx))
        cen2y.append(float(tmpy))
    if int(tmpc) == 3:
        cen3x.append(float(tmpx))
        cen3y.append(float(tmpy))
    if int(tmpc) == 4:
        cen4x.append(float(tmpx))
        cen4y.append(float(tmpy))
    if int(tmpc) == 5:
        cen5x.append(float(tmpx))
        cen5y.append(float(tmpy))
    if int(tmpc) == 6:
        cen6x.append(float(tmpx))
        cen6y.append(float(tmpy))
    
center0x = averagenum(cen0x)
center0y = averagenum(cen0y)
center1x = averagenum(cen1x)
center1y = averagenum(cen1y)
center2x = averagenum(cen2x)
center2y = averagenum(cen2y)
center3x = averagenum(cen3x)
center3y = averagenum(cen3y)
center4x = averagenum(cen4x)
center4y = averagenum(cen4y)
center5x = averagenum(cen5x)
center5y = averagenum(cen5y)
center6x = averagenum(cen6x)
center6y = averagenum(cen6y)
centerlist = [[center0x,center0y],[center1x,center1y],[center2x,center2y],[center3x,center3y],[center4x,center4y],[center5x,center5y],[center6x,center6y]]
for location in centerlist:
    print(location)
center = np.array(centerlist)




print(metrics.calinski_harabasz_score(raw,result))
# n_clusters=3 score= 2879.494940380821
# n_clusters=4 score= 2844.884151325418
# n_clusters=5 score= 11730.49107085872
# n_clusters=6 score= 11822.41624129993
# n_clusters=7 score= 12435.881769446121
# n_clusters=8 score= 12745.314456028627



plt.figure(figsize=(20,20))
plt.scatter(raw[:,1],raw[:,0],c=result,marker='.', zorder = 10, label = 'alcohol')
plt.scatter(center[:,1],center[:,0],marker='+',c='k', zorder = 20, label='center')
plt.title('Melbourne City Alcohol Distribution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()




#plt.plot(y, x, '.', label='Data', color='b')
#plt.xlabel('x')
#plt.ylabel('y')


#plt.show()










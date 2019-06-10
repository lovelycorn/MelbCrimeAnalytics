import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


f_in = open('./total_17_city.txt', 'r')
sumx = 0
sumy = 0
num = 0
for line in f_in:
    line = line.rstrip('\n')
    result = line.split(',')
    x = result[0]
    y = result[1]
    if float(x) >-37.8471 and float(x)<-37.7862:
        if float(y)>144.919 and float(y)<145.022:
            sumx += float(x)
            sumy += float(y)
            num += 1
print("the centre is ")
print(sumx/num,sumy/num)
center = np.array([[sumx/num,sumy/num]])
print(type(center))
print(center)

    










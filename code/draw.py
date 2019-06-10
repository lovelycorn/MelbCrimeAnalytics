import json
import re
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'
plt.figure(figsize=(20,20))
x,y = np.loadtxt('./beer_17.txt', delimiter=',', unpack=True)
plt.plot(y, x, '.', label='beer2017', color='b',alpha=0.7)
x,y = np.loadtxt('./wine_17.txt', delimiter=',', unpack=True)
plt.plot(y, x, '.', label='wine2017', color='r',alpha=0.5)
x,y = np.loadtxt('./whiskey_17.txt', delimiter=',', unpack=True)
plt.plot(y, x, '.', label='whiskey2017', color='y',alpha=0.4)
x,y = np.loadtxt('./vodka_17.txt', delimiter=',', unpack=True)
plt.plot(y, x, '.', label='vodka2017', color='c',alpha=0.3)
x,y = np.loadtxt('./tequila_17.txt', delimiter=',', unpack=True)
plt.plot(y, x, '.', label='tequila2017', color='k',alpha=0.1)
x,y = np.loadtxt('./brandy_17.txt', delimiter=',', unpack=True)
plt.plot(y, x, '.', label='brandy2017', color='m',alpha=0.2)


plt.xlabel('y')
plt.ylabel('x')
plt.title('Alcohol Type Distribution of Great Melbourne')
plt.legend()
plt.show()










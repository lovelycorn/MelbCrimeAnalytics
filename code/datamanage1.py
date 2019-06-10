import json

f1 = open("./ins17p1_raw.txt",'r')
f2 = open("./ins17p1_s1.txt",'a+')
num = 0
for line in f1 :
    strline = line
    newstr = strline[:-2] + "\n"
    f2.writelines(newstr)
    num += 1
    print(num)

f1.close()
f2.close()









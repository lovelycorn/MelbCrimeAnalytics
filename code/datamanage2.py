import json

f = open("./ins17p1_s1.txt",'r')
num = 0
for line in f :
    dic = json.loads(line)
    if "coordinates" in dic["doc"].keys():
        cod = dic["doc"]["coordinates"]["coordinates"]
        print(cod)
        print(type(cod))








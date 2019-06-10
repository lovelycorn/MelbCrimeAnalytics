import json

f1 = open("./ins18p4_raw.txt",'r')
f2 = open("./ins18p4_ok.txt",'a+')
num = 0
for line in f1 :
    if num == 0:
        num += 1
        continue

    strline = line
    newstr = strline[:-2] + "\n"
    dic = json.loads(newstr)
    if "coordinates" in dic["doc"].keys():
        cod = dic["doc"]["coordinates"]["coordinates"]
        x = cod[0]
        y = cod[1]
        if x is None or y is None :
            continue
        if x > -38 and x < -36:
            if y > 143 and y < 146:
                #data = [dic["doc"]["id"], dic["doc"]["tags"], dic["doc"]["caption"]["text"], dic["doc"]["user"]["username"], dic["doc"]["coordinates"]["coordinates"]]
                #print(type(data))
                #print(data)
                f2.writelines(newstr)
    num += 1
    print(num)

f1.close()
f2.close()









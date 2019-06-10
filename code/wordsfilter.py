import json
import re
def match(w_word, f_file, dic):
    if dic["doc"]["caption"]:
        if dic["doc"]["caption"]["text"]:
            text = dic["doc"]["caption"]["text"]
            if re.search(w_word, text, flags=re.IGNORECASE):
                x = dic["doc"]["coordinates"]["coordinates"][0]
                y = dic["doc"]["coordinates"]["coordinates"][1]
                newstr = str(x) + "," + str(y) + "\n"
                print(w_word+": "+text)
                print("text: "+newstr)
                f_file.write(newstr)
                return
    if dic["doc"]["tags"]:
        taglist = dic["doc"]["tags"]
        for tag in taglist:
            if re.search(w_word, tag, flags=re.IGNORECASE):
                x = dic["doc"]["coordinates"]["coordinates"][0]
                y = dic["doc"]["coordinates"]["coordinates"][1]
                newstr = str(x) + "," + str(y) + "\n"
                print(w_word+" :"+tag)
                print("tag: "+newstr)
                f_file.write(newstr)
                return
    return


f_raw = open("./ins17p4_ok.txt",'r')
f_beer = open("./beer_17.txt",'a+')
f_vodka = open("./vodka_17.txt",'a+')
f_wine = open("./wine_17.txt",'a+')
f_whiskey = open("./whiskey_17.txt",'a+')
f_brandy = open("./brandy_17.txt",'a+')
f_tequila = open("./tequila_17.txt",'a+')

num = 0
w_beer = r"beer"
w_vodka = r"vodka"
w_wine = r"wine"
w_whiskey = r"whiskey"
w_brandy = r"brandy"
w_tequila = r"tequila"
for line in f_raw :
    strline = line
    dic = json.loads(strline)       
    match(w_beer,f_beer,dic)
    match(w_vodka,f_vodka,dic)
    match(w_wine,f_wine,dic)
    match(w_whiskey,f_whiskey,dic)
    match(w_brandy,f_brandy,dic)
    match(w_tequila,f_tequila,dic)
    print(num)
    num += 1
f_raw.close()
f_beer.close()
f_vodka.close()
f_wine.close()
f_whiskey.close()
f_brandy.close()
f_tequila.close()


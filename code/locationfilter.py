f_out = open("./brandy_18_city.txt",'a+')
f_in = open('./brandy_18.txt', 'r')
for line in f_in:
    line = line.rstrip('\n')
    result = line.split(',')
    x = result[0]
    y = result[1]
    if float(x) < -37.6:
        if float(y)>144.66 and float(y)<145.26:
            str = x + "," + y + "\n"
            print(type(str))
            print(str)
            f_out.write(str)

    










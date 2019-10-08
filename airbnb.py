f = open('c:/users/surajit/desktop/first_10.csv')
for line in f:
    a=line.split(",")
    x = a[9]
    if(x != 'price'):
        if int(x) >= 100 and int(x) <=150:
            print(line)

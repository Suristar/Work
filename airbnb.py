import sys
file_name = sys.argv[1]
price_min = sys.argv[2]
price_max = sys.argv[3]
f = open(file_name)
for line in f:
    a=line.split(",")
    x = a[9]
    if(x != 'price'):
        if int(x) >= price_min and int(x) <=price_max:
            print(line)

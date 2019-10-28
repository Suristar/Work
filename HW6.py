import pandas as pd

import sys
file_name = sys.argv[0]
price_min = int(sys.argv[1])
price_max = int(sys.argv[2])

df = pd.read_csv(file_name) 
f = df.query("price >= price_min and price <= price_max")
print(f)
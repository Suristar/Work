import sys
file_name = sys.argv[0]
price_range = sys.argv[1]
Columns_separator = sys.argv[2]
Escape_character = sys.argv[3]

sys.argv[0] = 'c:/users/surajit/desktop/complete.csv'
f = open(sys.argv[0], encoding="utf-8")
lines = f.readlines()
for line in lines[1:]:
    columns = line.split(sys.argv[2])
    clean_columns = [] # this will contain the correctly-parsed columns
    in_quote = False  
    for x in columns: # we go through the "dirty" columns of data. We will set in_quote to True when we are inside a quote
        clean_x = x.replace(sys.argv[3], '') # we remove the "escaped" quotes from x
        n_quotes = clean_x.count(sys.argv[3])
        if not in_quote:
            clean_columns += [ clean_x ] # we aren't in a quote, we can add the column to the clean ones
            if n_quotes % 2 != 0:  # x contains an odd number of quotes, we will have to handle the next columns differently
                in_quote = True
        else:
            clean_columns[-1] += clean_x  # we are in a quote, we musn't create a new column. Instead, we append the current column to the last one in columns_clean
            if n_quotes % 2 != 0:  # this is our closing quote, next column will be out of the quote
                in_quote = False
    try:
        sys.argv[1] = int(clean_columns[9])
    except:
        print("Parsing ERROR: ",line)
        sys.exit(1)
    if sys.argv[1] >= 100 and sys.argv[1] <= 150:
        print(line)
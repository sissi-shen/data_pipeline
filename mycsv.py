import sys

def getdata():
    if len(sys.argv)==1: # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    return data.strip()

def readcsv(data):
    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """
    new_data = data.split('\n')
    col_header = new_data[0].split(',')
    headers = []
    for col in col_header:
        headers.append(col)

    data = []
    for r in new_data[1:]:
        ele = r.split(',')
        data.append(ele)

    return headers, data

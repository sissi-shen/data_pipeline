import json
from mycsv import *

headers, data = readcsv(getdata())

def csv_to_json(headers, data):
	# json_output = f""
    lines = []
    for line in data:
    	record = {}
    	for i in range(len(headers)):
    		record[headers[i]] = line[i]
    	lines.append(record)
    	
    json_dict = {"headers": headers, "data": lines}
    return json_dict

json_output = json.dumps(csv_to_json(headers, data))
print(json_output)

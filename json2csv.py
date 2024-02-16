import sys
import json

json_file = json.loads(open(sys.argv[1]).read())
csv_output = ''

for h in json_file['headers']:
	csv_output += f"{h},"

csv_output = csv_output.strip(",")

for record in json_file['data']:
	csv_output += "\n"+",".join(record.values())

print(csv_output)
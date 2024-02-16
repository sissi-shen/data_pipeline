import sys
import untangle
import xmltodict


xml = xmltodict.parse(open(sys.argv[1]).read())
csv_output = xml['file']['headers']

for line in xml['file']['data']['record']:
	csv_output += "\n"+",".join(line.values())

print(csv_output)

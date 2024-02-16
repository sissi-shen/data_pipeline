import sys
from mycsv import *

headers, data = readcsv(getdata())

my_html = f"\n<html>\n<body>\n<table>\n<tr>"

for header in headers:
	my_html += f"<th>{header}</th>"
my_html += f"</tr>\n"

for line in data:
	my_html += "<tr>"
	for ele in line:
		my_html += f"<td>{ele}</td>"
	my_html += f"</tr>\n"

my_html += "\n</table>\n</body>\n</html>\n\n"

print(my_html)

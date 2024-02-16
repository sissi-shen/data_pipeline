import sys
from mycsv import *

headers, data = readcsv(getdata())

my_xml = f'<?xml version="1.0"?>\n<file>\n<headers>'
my_xml+=','.join(headers)
my_xml+='</headers>\n<data>\n'
for row in data:
    my_xml+='<record>'
    for i in range(len(headers)):
        h = headers[i].replace(' ', '_')
        my_xml+=f'<{h}>'+ row[i]+f'</{h}>'
    my_xml+='</record>\n'
        
my_xml+='</data>\n</file>'

print(my_xml)




#!/usr/bin/python3

import csv
req_file="/home/ubuntu/PythonScripting/sample.csv"

fo=open(req_file,'r')
content=csv.reader(fo,delimiter=',')

#print(list(content))
#print(f'The header is:\n {list(content)[0]}')
#for papa in content:
#    print(papa)
#header=next(content)
print(list(content))
#print('The no. of rows are: ',len(list(content))-2)

fo.close()




'''
sfile="sample.csv"
dfile="sample1.csv"

sfo=open(sfile,'r')
content=sfo.read()
print(content)

sfo.close()

dfo=open(dfile,'w')
dfo.write(content)

dfo.close()
'''




'''
fo=open(sfile,'r')
content=sfo.read()
print(content)
print(sfo.mode)
sfo.close()

dfo=open(dfile,'w')
dfo.write(content)
print(dfo.mode)

dfo.close()
'''

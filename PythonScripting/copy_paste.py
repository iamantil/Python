#!/usr/bin/python3

sfile="random.txt"
dfile="newrandom.txt"

sfo=open(sfile,'r')
content=sfo.read()
print(content)
print(sfo.mode)
sfo.close()

dfo=open(dfile,'w')
dfo.write(content)
print(dfo.mode)

dfo.close()

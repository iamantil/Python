#!/usr/bin/python3

import csv

fname='demo.csv'
fo=open(fname,'w')
writer=csv.writer(fo,delimiter=",")
'''
writer.writerow(['S_No.','Name','Age','Sex'])
writer.writerow([1,'Jimmy',30,'F'])
'''
input_data=[['S_No.','Name','Age'],[1,'Jimmy',22],[2,'Soniya',28]]
writer.writerows(input_data)

fo.close()

#!/usr/bin/python

#There are 1,40,000 modules in python. Only few of them are listed using {help ("modules")} and they are the default.
#The remaining other modules are third party modules which needs to be installed manually as per the use case.
#xlwt is the module to write to excel sheets.
#xlrd is the module to read the excel sheets.
#boto3 is the module to work with AWS.
#paramiko is the module to work with remote servers.
#import math *
#import matth as m which means math module would be represented by m through the entire script.
#import math pi, pow here only two math operations are imported.
#different ways of importing modules:

a.) import math

syntax:
	print(math.pi)

b.) import math as m

syntax:
	print(m.pi)
c.) from math import *

syntax:
	print(pi)
	print(pow(4,2))
d.) from math import pi,pow

syntax:
	print(pi)
	print(pow(4,2))

#Install terraform module with pip install python-terraform
#To import the module use import python_terraform
#To get the details bout functions and operation of terraform use dir(python_terraform)
#To get details about how to use functions and operations use help(python_terraform)
#ls -lrt ---> to check if there is any soft link
#ln -s os_path.py myos ----> to create soft link of file' os_path.py' with name 'myos'

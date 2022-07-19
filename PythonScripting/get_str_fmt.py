#!/usr/bin/python3

usr_str=input('Please enter your string: ')

usr_inout=input('Do you want to convert the format of your string? ')

if usr_inout=='yes':
   print(usr_str.title())
else:
   print(usr_str)

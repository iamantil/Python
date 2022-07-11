#!/usr/bin/python3
import os
t_w=os.get_terminal_size().columns
#$tput cols to get the total number of columns in linux terminal
#display given string at right side or left side or center of a line in title format.
x=input("Enter your string: ")
print(x.center(t_w).title())
print(x.ljust(t_w).title())
print(x.rjust(t_w).title())
#print(x.title())

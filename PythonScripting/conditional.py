#!/usr/bin/python3
import os
t_w=os.get_terminal_size().columns

x=str(input("Enter your string: "))
print(x)
usr_cnf=str(input("Do you want to align your string over the terminal? "))
if usr_cnf=="yes":
        print(x.center(t_w).title())
        print(x.ljust(t_w).title())
        print(x.rjust(t_w).title())
#y=str(input("Do you want to align your string over the terminal? "))

#if y=="yes":
#   print(x.center(t_w).title)

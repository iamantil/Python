#!/usr/bin/python3

import os
path=input('Enter your path: ')

if os.path.exists(path):
   print(f'The {path}: is a vlaid path\n')
   if os.path.isfile(path):
      print(f'The {path}: is a file')
else:
   print(f'The {path}: is invalid, Please enter a valid path')

#!/usr/bin/python3

#This script is to clear the screen in Windows and linux OS.

import os
import platform

if platform.system()=='Linux':
   os.system('clear')
else:
   os.system('cls')

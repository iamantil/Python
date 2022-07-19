#!/usr/bin/python3

import os
'''
print(os.path.sep)
print(os.path.basename('/home/ubuntu/PythonScripting/modules/os_path.py'))
print(os.path.dirname('/home/ubuntu/PythonScripting/modules/os_path.py'))
path1="test"
path2="script"
print(os.path.join(path1,path2))
'''
path='/home/ubuntu/PythonScripting/modules/myos_softlink'
'''
print(os.path.split(path))
print(os.path.getsize('/home/ubuntu/PythonScripting/modules/os_path.py'))
'''
'''
#if os.path.exists(path):
#   print(f'{path}: is a file')
if os.path.isfile(path):
   print('{path}: is a file')
elif os.path.isdir(path):
   print('{path}: is a directory')

else:
   print(f'{path}: You have choosen an incorrect path please choose {path}')
'''

'''
if os.path.isfile(path):
   print(f'{path}: is a file')
else:
   print(f'{path}: is not a file')
'''
'''
if os.path.islink(path):
   print(f'{path}: Contains a soft link')
else:
   print(f'{path}: Do not have a soft link')

#print(os.path.islink('/home/ubuntu/PythonScripting/modules/myos_softlink'))
'''

print(os.path.getatime)

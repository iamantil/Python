#!/usr/bin/python3

valid_java=['1.6','1.7','1.8','1.9']
host_java=eval(input('Enter the host java version that you want to validate: '))
#host_java='1.5'

if host_java in valid_java:
   print('The host is deployed with valid java version')
else:
   print('The host is deployed with invalid java version')

db_users=['db_admin','db_config','db_analyst','db_installer']
valid_user=str(input('Enter the user name to validate the access over db: '))

if valid_user in db_users:
   print('The user is authorized to start the db')
else:
   print('invalid user')

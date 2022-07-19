#!/usr/bin/python3

num=eval(input('Please enter the number between 1 and 10: '))
'''
if user_num==1:
   print('one')
if user_num==2:
   print('two')
if user_num==3:
   print('three')
if user_num==4:
   print('four')
if user_num==5:
   print('five')
if user_num==6:
   print('six')
if user_num==7:
   print('seven')
if user_num==8:
   print('eight')
if user_num==9:
   print('nine')
if user_num==10:
   print('Ten')
else:
   print('The entered number is out of range please enter the number between 1 and 10: ')
'''
'''
#ranged_num=[1,2,3,4,5,6,7,8,9,10]
if num in [1,2,3,4,5,6,7,8,9,10]:
   if num==1:
      print('one')
   elif num==2:
      print('two')
   elif num==3:
      print('three')
   elif num==4:
      print('four')
   elif num==5:
      print('five')
   elif num==6:
      print('six')
   elif num==7:
      print('seven')
   elif num==8:
      print('eight')
   elif num==9:
      print('nine')
   elif num==10:
      print('ten')
else:
   print('The entered number is out of range please eneter between 1 and 10')
'''



num_word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'10'}
if num in [1,2,3,4,5,6,7,8,9,10]:
   print(num_word.get(num))
else:
   print('The entered number is out of range please eneter between 1 and 10')

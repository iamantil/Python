#!/usr/bin/python3

a=eval(input('Enter your first number: '))
b=eval(input('Enter your second number: '))

if a > b:
   print(f'The number {a} is greater than number {b}')
elif b > a:
   print(f'The number {b} is greater than number {a}')
else:
   print(f'The number {a} is equal to number {b}')

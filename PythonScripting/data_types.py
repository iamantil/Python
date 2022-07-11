#!/usr/bin/python3
x=10
y=100.0
z=10+100.0j

print(x, type(x))
print(y, type(y))
print(z, type(z))

my_name="Prashant"
print(my_name, type(my_name))


learning_python=True
learning_java=False

print(learning_python, type(learning_python))
print(learning_java, type(learning_java))

'''
Converting data tyoes in to one-another
'''
x=5
print(x, type(x))
y=str(x)
print(y, type(y))
z=bool(x)
print(z, type(z))
p=0
print(p, type(p))
q=bool(p)
print(q, type(q))

x=100.00
print(int(x))

my_name="Prashant"
print(my_name, type(my_name))
#print(int(my_name))

x="1.2.3.45"
print(x, type(x))


x="45"
print(type(x))
print(int(x))

#!/usr/bin/python3

#my_set={1,2,3,4,5,6,7,6,5,4,3,2,1}
#print(my_set)
#print(bool(my_set))

#my_set=({})
#print(bool(my_set),type(my_set))


#my_list=[1,4,2,5,3,6,7,8,7,6,1,2,4,3,4]
#set_output=set(my_list)
#print(set_output)

#print(dir(set))


a={1,2,3,4,5}
b={3,4,5,6,2}
union_output=a.union(b)
intersection_output=a.intersection(b)

print(union_output,intersection_output)

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:23:57 2019

@author: kumaran
"""
#remove the duplicate from the list
number=[4,5,5,5,5,5,7,85,4,5,4,4,52,2,8]
for i in number:
    print(i)
a=set(number)
b=list(set(number))
print('to remove duplicate element is',b)

#print the second largest number in the list
'''tens=[84,65,12,96,55,32,79]
tens.sort()
print('the second largest integer is',tens[-2])'''

#check the input value is integer or not
c=int(input('enter the value:'))

print("Type",type(c))
if type(c)==int:
    print('it is an interger')
else:
    print('it is not an integer')
 
#check the input value is postive or negative
'''num=int(input('enter the value'))
if num>0:
    print('it is positive')
else:
    print('it is negative')'''
a={1:"aravind",2:"ajith",3:"ram"}
numb=(1,2,34,56,63,7)

class test:
    def __init__(self,a=10,b=10):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)

a=test()
a.add()


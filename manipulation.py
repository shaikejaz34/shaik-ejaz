# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 08:16:59 2019

@author: shaik ejaz
"""

def manipulation():

  def add(x,y):
    z =  x+y
    return z,'addition'

  def sub(x,y):
    z = x-y
    return z,'subtraction'

  def multi(x,y):
    z = x*y
    return z,'multiplication'

  def div(x,y):
    z = x/y
    return z,'division'


  def default():
    return 'enter a valid choice'

  if choice == 1:
    return add(x,y)
  elif choice == 2:
    return sub(x,y)
  elif choice == 3:
    return multi(x,y)
  elif choice == 4:
    return div(x,y)
  else:
    return default()

x = int(input('enter x value:'))
y = int(input('enter y value:'))


print('Enter Your Choice:')
choice = int(input('1.sum\n2.sub\n3.multi\n4.div\n:'))
r,s = manipulation(x,y,choice)

if r == 'invalid':
  print(s)
else:
  print('{0} of {1} and {2} is {3}'.format(s,x,y,r))
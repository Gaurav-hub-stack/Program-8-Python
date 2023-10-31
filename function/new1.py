#function 
def colors():
	print("red")
	print("green")

def colors():
   print("black")
   print("white")
a=2#this global varible 
b=3

def mul():
	a=10#new local to mul
	b=20
	print(a*b)
mul()

def add():
	print(a+b)

add()
#local Vs Global
#var defines inside fun def is known as local and other 
#var are know as global
#local var can be accesssed within it s enclosing scope
#where as global var cAN ACCESSED any where in program

def mul():
	global a,b,c
	a=10
	b=20
	c=a*b

#parameter is local scope
def mul(a,b):#a and b are parameters
    print(a*b)
mul(4,5)


i=int(input("enter 1st num:"))
j=int(input("enter 2st num:"))
mul(i,j)


#parameter
#always varibles
#duplicate params are not allowed
#def time concept


#argument
#var/val/exp
#allowed
#calling


#Type of Arguments 
#>Positional Arguments
#>Keyword Arguments
#>Default Arguments

def show(a,b=2):
	  print(a,b)
show(2,3)
show(a=2,b=3)
show(a=2)

def show(a,b):
	print(a,b)


#Type of parameters
#1.Positional only
#all params before /become pos only i.e can acept 
#only pos args
def show(a,b,/):
	print(a,b)
show(2,4)
#sho(a=1,b=2)#error

#2. Keyword only 
1#all param after * become keyword only i.e can accept
def show (*,a,b):
	print(a,b)

show(a=1,b=2)
#show(1,2) #error
#3.Positional or keyword
def show(a,b):
	print(a,b)
show(1,2)
show(a=1,b=2)
#4.Variable length position on

def show (*a):
	print(a)
show (10,20,30)
show(10,20)
show()
show(1,2,3,4,5,6,)
#5.Variable length keyword only
#it cAn accept o-n keyword args and all args are received in 
def show(**a):
    print(a)
show(i=10,j=10)

#example

def calc(a,b):
    c=a+b
    d=a-b
    e=a*b

print(calc(20,5))
#module name must not contain special char
#first char must be letter or undersore
#import p142
print(p156.add(3,5))
print(p145.mul(3,6))

import p45 as m1#m1 is alias 
print(m1.add(3,5))
print(m1.mul(3,5))

from p45 import add,mul
print(add(4,5))
print(mul(4,5))

from p156 import *
print(add(4,5))
print(mu(4,5))
#to add pakage in function
import myoack.p156 as m1
print(m1.add(1,5))


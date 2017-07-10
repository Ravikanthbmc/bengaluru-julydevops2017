#!/usr/bin/python

#from myclass import MyClass
from myclass import * 

print 'This is a print statement'
print( 'This is outside the sayHello function' )

def sayHello(): 
   print( 'This is from sayHello function - Hello Python!' ) 

#sayHello()

if __name__ == "__main__":
    obj = MyClass()
    obj.printValues()
    sayHello()

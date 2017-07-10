#!/usr/bin/python

class MyClass:

    def __init__(self):
        print ( 'This is a python constructor' )
        self.x = 100
        self.y = 200
    
    def printMemberVariableTypes(self):
        print ( 'Type of x is ', type( self.x ) )
        print ( 'Type of y is ', type( self.y ) )

        print ( 'Type of x is ', type( self.x ) )
        print ( 'Type of y is ', type( self.y ) )

    def setXandY(self, value1, value2):
        self.x = value1
        self.y = value2

    def printValues(self):
        print ( 'Value of X is ' + str(self.x) )
        print ( 'Value of Y is ' + str(self.y) )


def main():
   #first object of MyClass or instance 
   print ('First instance')
   obj1 = MyClass()
  # obj1.printMemberVariableTypes()

   print('Values after calling constructor')
   obj1.printValues()
   print('Values after calling set function')
   obj1.setXandY( 5, 10 )
   obj1.printValues()

   #second object of MyClass or instance 
   print ('Second instance')
   obj2 = MyClass()
   print('Values after calling constructor')
   obj2.printValues()
   #obj2.printMemberVariableTypes()

   obj2.setXandY( 50, 100 )
   print('Values after calling set function')
   obj2.printValues()

if __name__ == "__main__":
    main()

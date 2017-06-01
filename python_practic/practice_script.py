'''
little adding
this script contains an example class that we will write. the class will be called algebra, and it will contain some simple methods to do some algebraic manipulation.

this script will end with a sample way to call and use the class.



'''
sample_int = 5
print sample_int
class algebra:

    def __init__(self,x,y):
        # we are defining the arguments as attributes of
        # the object itself.
        self.x = x
        self.y = y
        
    def add( self ) :
        return self.x + self.y


    def subtract( self ) :
        return self.x - self.y

    def divide( self ) :
        return self.x/self.y

    def multiply( self ) :
        return self.x* self.y

  
    def complicated(self):
        return self.multiply() + self.add()

    def modify_x(self):
        self.x = self.x *2
        
if __name__ == "__main__":
    # create instance of algebra

    myalg = algebra(100,150)

    #print some outputs using the algebra class
    print myalg.multiply()
    myalg.modify_x()
    print myalg.multiply()

else:
    print "name not equal to main"
    print __name__
    

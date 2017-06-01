'''
here is the docstring:
we will use this to see how we can import from another module


'''
#adding comment
import practice_script as ps

print ps.sample_int
myalg = ps.algebra(1.5,5.0)
myalg.multiply()
print myalg.multiply()

for x in [1,3,5]:
    # lets loop over differnet values for the first argument in the
    #algebra class
    myalg = ps.algebra(x,5.0)
    print myalg.add()
    print myalg.x
    print myalg.y

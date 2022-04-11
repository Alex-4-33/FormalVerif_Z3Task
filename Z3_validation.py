from z3 import *

x = Int('x')
y = Int('y')

s = Solver()

s.add(ForAll([x, y], Implies(And((x + y > -5), (x - y < 5)), Or((2*x - y < 15), (x + 3*y > 7)))))
print (s.check())
print (s.model())

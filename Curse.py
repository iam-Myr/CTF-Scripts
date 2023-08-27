#!/usr/bin/python3
from z3 import *

# Create a Z3 solver instance
solver = Solver()

# Define the maximum length of the string
max_length = 16

# Define the array of BitVecs
x = [BitVec('x{}'.format(i), 64) for i in range(max_length)]

#ASCII Constraint
#for i in range(16):
 # solver.add(x[i] >= 0x20)
 # solver.add(x[i] <= 0x7f)

#Constraints
solver.add(x[0] == 112)
solver.add(x[3] == 104)
solver.add(x[10] == 95)
solver.add(x[5] == 110)
solver.add(x[6] ^ x[10] == 0)
solver.add(x[12] == 115)
solver.add(x[8] == x[7]-x[0] + 49)
solver.add(x[2] == x[0] - x[1] + 125)
solver.add(x[14] == 101)
solver.add(x[0] == x[1] - 9)
solver.add(x[9] == 118)
solver.add(x[11] == 49)
solver.add(x[7] - x[0] == 2)
solver.add(x[4] == ord("0"))
solver.add(x[13] == x[6]) 
solver.add(x[15] == ord("z"))   

# Check if the constraints are satisfiable
if solver.check() == sat:
    model = solver.model()
    # Retrieve the values of the array elements from the model
    array_values = [model[x[i]].as_signed_long() if model[x[i]] is not None else None for i in range(max_length)]
    # Filter out None values (end of string)
    string_values = filter(lambda x: x is not None, array_values)
    # Convert the values to characters
    string = ''.join(chr(value) for value in string_values)
    print("Decoded string:", string)
else:
    print("Constraints are unsatisfiable.")

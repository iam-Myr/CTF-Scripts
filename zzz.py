from z3 import *

# Create a Z3 solver instance
solver = Solver()

# Define the maximum length of the string
max_length = 30

# Define the array of BitVecs
x = [BitVec('x{}'.format(i), 64) for i in range(max_length)]

#ASCII Constraint
for i in range(30):
  solver.add(x[i] >= 0x20)
  solver.add(x[i] <= 0x7f)

#Constraints
solver.add(x[1] == x[2])
solver.add(x[3] | x[6] == 122)
solver.add(x[1] == x[2])
solver.add(x[3] | x[6] == 122)
solver.add(x[3] & x[6] == 66)
solver.add(x[4] == x[28])
solver.add(x[5] * x[29] == 15375)
solver.add(x[7] + x[6] + x[8] == 302)
solver.add(x[6] * x[7] - x[8] == 10890)
solver.add(x[9] - x[8] == 5)
solver.add(x[10]-x[9] == 27)
solver.add(x[11] ^ x[10] ==32)
solver.add(x[12] == x[15])
solver.add(x[12] + x[11] == 180)
solver.add(x[13] + x[12] == 185)
solver.add(x[14] + x[13] - x[16] == x[13])
solver.add(x[16] + x[17] == 217)
solver.add(x[17] == x[13])
solver.add(x[16] + x[14] == 2 * x[14])
solver.add(x[18] == 90)
solver.add(x[18] == x[19])
solver.add(x[20] ^ x[19] ^ x[21] == 127)
solver.add(x[22] ^ (x[21] ^ x[20]) == x[21])
solver.add(x[21] == 95)
solver.add(x[24] + x[6] == 180)
solver.add(x[25] == x[9])
solver.add(x[26] + x[27] == 212)
solver.add(x[27] == x[28])
#solver.add(x[23] + x[24] == -33) <- Problem constraint


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

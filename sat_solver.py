from z3 import *

x = BitVec('x',32)
y = BitVec('y',32)

solver = Solver()

solver.add(35 * (((3 * x) ^ 0xB6D8) % 0x521) % 0x5EB == 1370)
solver.add((35 * ((5 * y % 0x1E61) | 0x457) - 5) % 0x3E8 == 80)
solver.add(x % y == 20202020)
solver.add(y * x == 0x33D5D816326AAD)

print(solver.check())
print(solver.model())

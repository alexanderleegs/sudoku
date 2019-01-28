#!/usr/bin/env python
import sys
from sudoku.Generator import *

gen = Generator()
gen.generate_puzzle(4)
gen.show_puzzle()
print("-------------------------------------")
gen.show_solution()
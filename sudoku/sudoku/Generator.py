from sudoku.Board import *
import random

class Generator:
	def __init__(self):
		self.completed = None
		self.given = None
	
	def generate_puzzle(self, difficulty):
		# Generates a random completed sudoku puzzle
		puzzle = Board([0 for i in range(81)])
		puzzle.solve_board()
		self.completed = puzzle
		hint_num = 30 + (4 - difficulty) * 8
		# Randomly select positions to be clues
		ls = list(range(81))
		# Try until set of clues given produce a unique solution
		while True:
			random.shuffle(ls)
			clues = ls[:hint_num]
			starting = [0 for i in range(81)]
			for i in clues:
				starting[i] = self.completed.get_data()[i]
			possible = Board(starting)
			if (possible.check_unique()):
				self.given = possible
				break

	def show_puzzle(self):
		self.given.print_board()

	def show_solution(self):
		self.completed.print_board()




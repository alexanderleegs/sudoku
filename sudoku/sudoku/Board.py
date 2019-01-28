from sudoku.Cell import *
import random

class Board:
	def __init__(self, data):

		def get_parameters(cell_num):
			row = cell_num // 9
			col = cell_num % 9
			box = (row // 3) * 3 + col // 3
			return row, col, box

		# Each row, col and box has a bitmask stored indicating which numbers are already used
		self.data = data
		self.unfilled = []
		self.rows = [0 for i in range(9)]
		self.cols = [0 for i in range(9)]
		self.boxes = [0 for i in range(9)]
		self.moves = []
		self.solved = False
		for cell_num, val in enumerate(data):
			# Store unfilled cells and numbers used in each row, col, box
			row, col, box = get_parameters(cell_num)
			if (val == 0):
				new_cell = Cell(row, col, box, cell_num)
				self.unfilled.append(new_cell)
			else:
				val = val - 1
				self.rows[row] = self.rows[row] | (1 << val)
				self.cols[col] = self.cols[col] | (1 << val)
				self.boxes[box] = self.boxes[box] | (1 << val)

	def make_move(self, r, c, val):
		cell_num = r * 9 + c
		box = (r // 3) * 3 + c // 3
		
		if val == 0:
			# Removing a number
			original = self.data[cell_num]
			if (original != 0):
				shifted = 1 << (original - 1)
				self.rows[r] = self.rows[r] ^ shifted
				self.cols[c] = self.cols[c] ^ shifted
				self.boxes[box] = self.boxes[box] ^ shifted
		else:
			shifted = 1 << (val - 1)
			self.rows[r] = self.rows[r] | shifted
			self.cols[c] = self.cols[c] | shifted
			self.boxes[box] = self.boxes[box] | shifted

		self.data[cell_num] = val

	def solve(self, idx):
		if (idx == len(self.unfilled)):
			# Board has been completed
			return True
		else:
			curr_cell = self.unfilled[idx]
			row = curr_cell.get_row()
			col = curr_cell.get_col()
			box = curr_cell.get_box()
			bm = self.rows[row] | self.cols[col] | self.boxes[box]
			poss = []
			for i in range(9):
				digit = bm & 1
				bm = bm >> 1
				if (digit == 0):
					poss.append(i)
			random.shuffle(poss)
			for i in poss:
				self.make_move(row,col,i + 1)
				res = self.solve(idx+1)
				if (res):
					# Answer found
					return True
				self.make_move(row,col,0)
			# No answer works, must backtrack
			return False

	def solve_board(self):
		self.solve(0)

	def solve_unique(self, idx):
		if (idx == len(self.unfilled)):
			if (self.solved):
				# Board has been completed once before
				return True
			else:
				# First solution found
				self.solved = True
				return False
		else:
			curr_cell = self.unfilled[idx]
			row = curr_cell.get_row()
			col = curr_cell.get_col()
			box = curr_cell.get_box()
			bm = self.rows[row] | self.cols[col] | self.boxes[box]
			for i in range(9):
				digit = bm & 1
				bm = bm >> 1
				if (digit == 0):
					self.make_move(row,col,i + 1)
					res = self.solve_unique(idx+1)
					if (res):
						# Answer found
						return True
					self.make_move(row,col,0)
			# No answer works, must backtrack
			return False

	def check_unique(self):
		self.solved = False
		return not self.solve_unique(0)

	def print_board(self):
		print("-------------------------")
		for i in range(9):
			st = "| "
			for j in range(9):
				st += str(self.data[i * 9 + j])
				st += " "
				if j % 3 == 2:
					st += "| "
			print(st)
			if (i % 3 == 2):
				print("-------------------------")

	def get_data(self):
		return self.data


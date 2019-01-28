class Cell:
	def __init__(self, row, col, box, val):
		self.row = row
		self.col = col
		self.box = box
		self.val = val

	def get_row(self):
		return self.row

	def get_col(self):
		return self.col

	def get_box(self):
		return self.box

	def get_val(self):
		return self.val

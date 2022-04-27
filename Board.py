from pieces import Pawn, Rook, Bishop, Queen, King, Knight


class Board:
	'''This is the board class of the chess game.'''

	def __init__(self, pieces: list) -> None:
		'''
		Parameters
		----------
				pieces : list
						List of all the pieces to put on the board
		'''
		self.pieces = pieces
		self.board = [
			["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
			[],
			[],
			[],
			[],
			[],
			[],
			["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
		]
		# keeps record of all the pieces (location, eaten or not)
		self.record = {}
		self.grave = []
		self.init_board()
		self.print_board()
		self.update_record()
		print(self.record)

	def print_board(self):
		'''Constructs the board'''
		for i in self.board:
			print(i)
			print()
			print()

	def init_board(self):
		'''Initializes the board, placing pieces in it'''
		for j in self.pieces[:8]:  # add black pawns to the list
			if isinstance(j, Pawn) and j.team == 'black':
				self.board[1].append(j.__str__())

		for temp in self.board[2:6]: # Blank spaces in the middle
			for i in range(8):
				temp.append("    ")

		for j in self.pieces[8:16]:  # add white pawns to the list
			if isinstance(j, Pawn) and j.team == 'white':
				self.board[6].append(j.__str__())

		for r in self.pieces[16:20]:
			if isinstance(r, Rook) and r.team == 'white':
				if self.board[7][0] == "  ":
					self.board[7][0] = r.__str__()
				else:
					self.board[7][7] = r.__str__()
			elif isinstance(r, Rook) and r.team == 'black':
				if self.board[0][0] == "  ":
					self.board[0][0] = r.__str__()
				else:
					self.board[0][7] = r.__str__()
		
		for n in self.pieces[20:24]:
			if isinstance(n, Knight) and n.team == 'white':
				if self.board[7][1] == "  ":
					self.board[7][1] = n.__str__()
				else:
					self.board[7][6] = n.__str__()
			elif isinstance(n, Knight) and n.team == 'black':
				if self.board[0][1] == "  ":
					self.board[0][1] = n.__str__()
				else:
					self.board[0][6] = n.__str__()

		for b in self.pieces[24:28]:
			if isinstance(b, Bishop) and b.team == 'white':
				if self.board[7][2] == "  ":
					self.board[7][2] = b.__str__()
				else:
					self.board[7][5] = b.__str__()
			elif isinstance(b, Bishop) and b.team == 'black':
				if self.board[0][2] == "  ":
					self.board[0][2] = b.__str__()
				else:
					self.board[0][5] = b.__str__()

		self.board[0][3] = self.pieces[28].__str__() # Queens
		self.board[7][4] = self.pieces[29].__str__()
		self.board[0][4] = self.pieces[30].__str__() # Kings
		self.board[7][3] = self.pieces[31].__str__()

	def update_record(self):
		'''Updates the record of the pieces coordinates'''
		for i in self.pieces:
			self.record[i.__str__()] = i.get_position()


def let_to_num(row_let):
	'''Changes the letters to numbers'''
	match row_let:
		case "A":
			return 0
		case "B":
			return 1
		case "C":
			return 2
		case "D":
			return 3
		case "E":
			return 4
		case "F":
			return 5
		case "G":
			return 6
		case "H":
			return 7
	return "OOPS, NOT ON THE BOARD"


# Set up all the pieces in vars
p1 = Pawn('black', 'P01', [let_to_num("A"), 1])
p2 = Pawn('black', 'P02', [let_to_num("B"), 1])
p3 = Pawn('black', 'P03', [let_to_num("C"), 1])
p4 = Pawn('black', 'P04', [let_to_num("D"), 1])
p5 = Pawn('black', 'P05', [let_to_num("E"), 1])
p6 = Pawn('black', 'P06', [let_to_num("F"), 1])
p7 = Pawn('black', 'P07', [let_to_num("G"), 1])
p8 = Pawn('black', 'P08', [let_to_num("H"), 1])
p9 = Pawn('white', 'P09', [let_to_num("A"), 1])
p10 = Pawn('white', 'P10', [let_to_num("B"), 1])
p11 = Pawn('white', 'P11', [let_to_num("C"), 1])
p12 = Pawn('white', 'P12', [let_to_num("D"), 1])
p13 = Pawn('white', 'P13', [let_to_num("E"), 1])
p14 = Pawn('white', 'P14', [let_to_num("F"), 1])
p15 = Pawn('white', 'P15', [let_to_num("G"), 1])
p16 = Pawn('white', 'P16', [let_to_num("H"), 1])

r1 = Rook('black', 'R01', [let_to_num("A"), 1])
r2 = Rook('black', 'R02', [let_to_num("H"), 1])
r3 = Rook('white', 'R03', [let_to_num("A"), 1])
r4 = Rook('white', 'R04', [let_to_num("H"), 1])

n1 = Knight('white', 'N01', [let_to_num("B"), 1])
n2 = Knight('white', 'N02', [let_to_num("G"), 1])
n3 = Knight('black', 'N03', [let_to_num("B"), 1])
n4 = Knight('black', 'N04', [let_to_num("G"), 1])

b1 = Bishop('white', 'B01', [let_to_num("C"), 1])
b2 = Bishop('white', 'B02', [let_to_num("F"), 1])
b3 = Bishop('black', 'B03', [let_to_num("C"), 1])
b4 = Bishop('black', 'B04', [let_to_num("F"), 1])

q1 = Queen('black', 'Q01', [let_to_num("D"), 1])
q2 = Queen('white', 'Q02', [let_to_num("E"), 1])

k1 = King('black', 'K01', [let_to_num("E"), 1])
k2 = King('white', 'K02', [let_to_num("D"), 1])

list1 = [
	p1, p2, p3, p4,
	p5, p6, p7, p8,
	p9, p10, p11, p12,
	p13, p14, p15, p16,
	r1, r2, r3, r4,
	n1, n2, n3, n4,  # Knights
	b1, b2, b3, b4,
	q1, q2,
	k1, k2
]

gameOver = False
whiteTurn = False

def main():
	board = Board(list1)
	while not gameOver:
		piece = input('Enter the name of the piece to be moved: ')

		if whiteTurn:
			if 'w' not in piece:
				print("It has to be a white piece")
			else:
				row = let_to_num(input('Enter the target row: ').upper())
				col = int(input('Enter the target column: ')) - 1
		else:
			if 'b' not in piece:
				print("It has to be a white piece")
			else:
				row = let_to_num(input('Enter the target row: ').upper())
				col = int(input('Enter the target column: ')) - 1
				target = [row, col]



		pass


Board(list1)



class Matrix:
	def __init__(self, *args):
		self.matrix = []
		if (len(args) > 1):
			for var in args:
				self.matrix.append(var)
		else:
			self.matrix = args[0]
	#вывод на экран
	def print_matrix(self):
		for var in self.matrix:
			for i in var:
				print(i, end= " ")
			print()

	#переопределение знаков
	def __eq__(self, other):
		return not self.det_matrix() - other.det_matrix()

	def __ne__(self, other):
		return self.det_matrix() - other.det_matrix() == 0

	def __gt__(self, other):
		return self.det_matrix() > other.det_matrix()

	def __lt__(self, other):
		return self.det_matrix() < other.det_matrix()

	def __ge__(self, other):
		return self.det_matrix() >= other.det_matrix()

	def __le__(self, other):
		return self.det_matrix() <= other.det_matrix()

	# детерминант 

	def minor_matrix(self,i,j):
		return [row[:j] + row[j+1:] for row in (self.matrix[:i]+self.matrix[i+1:])]

	def det_matrix(self):
		if len(self.matrix) == 1 :return self.matrix[0][0]
		if len(self.matrix) == 2:
			return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

		det = 0
		for i in range(len(self.matrix)):
			new_matrix = Matrix(self.minor_matrix(0, i))
			det += (-1) ** i * self.matrix[0][i] * new_matrix.det_matrix()
		return det



	#сложение
	def __add__(self, other):
		result_add = [[] * len(self.matrix)]* len(self.matrix)
		result_add = [[self.matrix[i][j] + other.matrix[i][j] for j in range (len(self.matrix[0]))] for i in range(len(self.matrix))]
		return result_add
	#умножение
	def __mul__(self, other):
		result_mul = [[0 for col in range(len(self.matrix[0]))] for row in range(len(other.matrix))]
		for i in range(len(self.matrix)):
			for j in range(len(other.matrix[0])):
				for k in range(len(other.matrix)):
					result_mul[i][j] += self.matrix[i][k] * other.matrix[k][j]
		return result_mul


m1 = Matrix([4, 2, 5], [7, 6, 5], [9, 7, 6])
m2 = Matrix([4, 3, 8], [12, 6, 1], [9, 3, 5])
m1.print_matrix()
m2.print_matrix()
print(m1.det_matrix())
print(m2.det_matrix())
print(m1 > m2)

m = Matrix(m1 * m2)
mm = Matrix(m1 + m2)
m.print_matrix()
mm.print_matrix()
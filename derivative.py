from __future__ import division

class Dual(object):
	"""
	Represents a number of the form a + b * e, where e != 0
	but e^2 = 0.
	"""
	def __init__(self, a=0.0, b=0.0):
		self.a = a
		self.b = b

	def __add__(self, other):
		if isinstance(other, Dual):
			return Dual(self.a + other.a, self.b + other.b)
		else:
			return Dual(self.a + other, self.b)

	def __radd__(self, other):
		if isinstance(other, Dual):
			return Dual(self.a + other.a, self.b + other.b)
		else:
			return Dual(self.a + other, self.b)

	def __sub__(self, other):
		if isinstance(other, Dual):
			return Dual(self.a - other.a, self.b - other.b)
		else:
			return Dual(self.a - other, self.b)

	def __rsub__(self, other):
		if isinstance(other, Dual):
			return Dual(other.a - self.a, other.b - self.b)
		else:
			return Dual(other - self.a, self.b)

	def __mul__(self, other):
		if isinstance(other, Dual):
			return Dual(self.a * other.a, self.b * other.a + other.b * self.a)
		else:
			return Dual(self.a * other, self.b * other)

	def __rmul__(self, other):
		if isinstance(other, Dual):
			return Dual(self.a * other.a, self.b * other.a + other.b * self.a)
		else:
			return Dual(self.a * other, self.b * other)

	def __str__(self):
		if self.b == 0:
			return str(self.a)
		elif self.b > 0:
			return '{} + {}e'.format(self.a, self.b)
		elif self.b < 0:
			return '{} - {}e'.format(self.a, -self.b)

def derive(f, x):
	"""
	Returns the derivative of `f` at position `x`.
	"""
	return f(Dual(x, 1)).b

if __name__ == '__main__':
	f = lambda x: x * 5 + 2 * (x * x + 3)
	print(derive(f, 3))
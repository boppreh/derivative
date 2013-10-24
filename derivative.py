from __future__ import division

class Dual(object):
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

	def __truediv__(self, other):
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

x = Dual(1, 1)
y = Dual(3, -5)
print(x * y)
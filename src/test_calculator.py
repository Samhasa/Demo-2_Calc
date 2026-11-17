import unittest

from calculator import calculator


class CalculatorTests(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calculator("add", 7, 3), 10)

	def test_subtract(self):
		self.assertEqual(calculator("subtract", 7, 3), 4)

	def test_multiply(self):
		self.assertEqual(calculator("multiply", 7, 3), 21)

	def test_divide(self):
		self.assertEqual(calculator("divide", 7, 2), 3.5)

	def test_divide_by_zero_raises_value_error(self):
		with self.assertRaises(ValueError):
			calculator("divide", 7, 0)

	def test_invalid_operation_raises_value_error(self):
		with self.assertRaises(ValueError):
			calculator("modulo", 7, 3)


if __name__ == "__main__":
	unittest.main()

from unittest import TestCase
from functions import divide, multiply


class TestFunctions(TestCase):
    def test_divide(self):
        dividend, divisor, expected_result = (15, 3, 5.0)

        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_negative(self):
        dividend, divisor, expected_result = (15, -3, -5.0)

        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_dividend_zero(self):
        dividend, divisor, expected_result = (0, 5, 0.0)

        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_error_on_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(25, 0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected_result = 15
        self.assertEqual(multiply(expected_result), expected_result)

    def test_multiply_zero(self):
        expected_result = 0
        self.assertEqual(multiply(expected_result), expected_result)

    def test_multiply_result(self):
        inputs, expected_result = ((3, 5), 15)

        self.assertEqual(multiply(*inputs), expected_result)

    def test_multiply_result_with_zero(self):
        inputs, expected_result = ((3, 5, 0), 0)

        self.assertEqual(multiply(*inputs), expected_result)

    def test_multiply_negative(self):
        inputs, expected_result = ((3, -5, 2), -30)

        self.assertEqual(multiply(*inputs), expected_result)

    def test_multiply_floats(self):
        inputs, expected_result = ((3.0, 2), 6.0)

        self.assertEqual(multiply(*inputs), expected_result)

import unittest
import testaus.calculator.calculator as calculator


class TestSumma(unittest.TestCase):
    def test_summa_returns_sum_of_integers(self):
        result = calculator.summa(2, 3)
        self.assertEqual(result, 5)  # add assertion here

    def test_summa_returns_sum_of_floats(self):
        result = calculator.summa(2.2, 3.8)
        self.assertEqual(result, 6)  # add assertion here

    def test_summa_works_with_negative_numbers(self):
        result = calculator.summa(-1,-10)
        self.assertEqual(result, -11)  # add assertion here

    def test_summa_returns_sum_of_integer_and_float(self):
        result = calculator.summa(10, 5.1)
        self.assertEqual(result, 15.1)  # add assertion here

    def test_summa_returns_sum_of_negative_and_positive(self):
        result = calculator.summa(-100,100)
        self.assertEqual(result, 0)  # add assertion here

    def test_summa_returns_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.summa(10, "10")

class TestJako(unittest.TestCase):

    def test_jako_returns_div_of_integers(self):
        result = calculator.jako(10, 2)
        self.assertEqual(result, 5)

    def test_jako_returns_div_of_floats(self):
        result = calculator.jako(1.5, 0.1)
        self.assertEqual(result, 15)

    def test_jako_returns_div_of_integer_and_float(self):
        result = calculator.jako(5.2, 2)
        self.assertEqual(result, 2.6)

    def test_jako_returns_div_of_negative_numbers(self):
        result = calculator.jako(-10, -2)
        self.assertEqual(result, 5)

    def test_jako_returns_div_of_positive_and_negative(self):
        result = calculator.jako(-10, 2)
        self.assertEqual(result, -5)

    def test_jako_returns_div_of_integer_into_float(self):
        result = calculator.jako(10, 3)
        self.assertEqual(result, 3.3333333333333335)

    def test_jako_returns_error_if_not_number(self):
        with self.assertRaises(TypeError):
            calculator.jako(10, "juukelis")

    def test_jako_returns_zerodivision_error(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.jako(10, 0)


class TestKerto(unittest.TestCase):

    def test_kerto_returns_mul_of_integers(self):
        result = calculator.kerto(10, 2)
        self.assertEqual(result, 20)

    def test_kerto_returns_mul_of_floats(self):
        result = calculator.kerto(1.5, 0.5)
        self.assertEqual(result, 0.75)

    def test_kerto_returns_mul_of_integer_and_float(self):
        result = calculator.kerto(10, 0.5)
        self.assertEqual(result, 5)

    def test_kerto_returns_mul_of_negatives(self):
        result = calculator.kerto(-10, -2)
        self.assertEqual(result, 20)

    def test_kerto_returns_mul_of_negative_and_positive(self):
        result = calculator.kerto(-10, 2)
        self.assertEqual(result, -20)

    def test_kerto_raises_type_error(self):
        with self.assertRaises(TypeError):
            calculator.kerto("puukelis", "juukelis")


class TestMiinus(unittest.TestCase):

    def test_kerto_returns_min_of_integers(self):
        result = calculator.miinus(10, 2)
        self.assertEqual(result, 8)

    def test_kerto_returns_min_of_floats(self):
        result = calculator.miinus(10, 2)
        self.assertEqual(result, 8)

    def test_kerto_returns_min_of_integer_and_float(self):
        result = calculator.miinus(10, 2)
        self.assertEqual(result, 8)

    def test_kerto_returns_min_of_positive_and_negative(self):
        result = calculator.miinus(10, 2)
        self.assertEqual(result, 8)

    def test_kerto_returns_min_of_negatives(self):
        result = calculator.miinus(10, 2)
        self.assertEqual(result, 8)

    def test_miinus_raises_type_error(self):
        with self.assertRaises(TypeError):
            calculator.miinus("puukelis", "juukelis")


if __name__ == '__main__':
    unittest.main()

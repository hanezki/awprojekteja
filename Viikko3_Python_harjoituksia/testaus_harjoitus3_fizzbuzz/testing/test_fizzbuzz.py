import unittest
import fizzbuzz.fizzbuzz as fizz

class MyTestCase(unittest.TestCase):

    def test_fizzbuzz_works_with_5_and_3(self):
        result = fizz.fizzbuzz(15)
        self.assertEqual(result, "FizzBuzz")  # add assertion here

    def test_fizzbuzz_works_with_5(self):
        result = fizz.fizzbuzz(10)
        self.assertEqual(result, "Buzz")  # add assertion here

    def test_fizzbuzz_works_with_3(self):
        result = fizz.fizzbuzz(9)
        self.assertEqual(result, "Fizz")  # add assertion here

    def test_fizzbuzz_works_other_numbers(self):
        result = fizz.fizzbuzz(16)
        self.assertEqual(result, 16)  # add assertion here

    def test_fizzbuzz_raises_type_error(self):
        with self.assertRaises(TypeError):
            result = fizz.fizzbuzz("juukeli")


if __name__ == '__main__':
    unittest.main()

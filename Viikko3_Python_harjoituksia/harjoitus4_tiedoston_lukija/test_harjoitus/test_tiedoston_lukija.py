import unittest
import harjoitus.tiedoston_lukija as lukija


class MyTestCase(unittest.TestCase):

    def test_lukija_works_with_empty_file(self):
        result = lukija.lue("empty_teksti.txt", 1)
        self.assertEqual(result, "Empty file.")  # add assertion here

    def test_lukija_works_with_no_file(self):
        result = lukija.lue("asdasdsad.txt", 1)
        self.assertEqual(result, "File not found.")  # add assertion here

    def test_lukija_works_with_wrong_index(self):
        with self.assertRaises(IndexError):
            result = lukija.lue("teksti.txt", 100)

    def test_lukija_works_with_correct_settings(self):
        result = lukija.lue("teksti.txt", 0)
        self.assertEqual(result, "rivi 1.")  # add assertion here

    def test_lukija_works_with_correct_settings_2(self):
        result = lukija.lue("teksti.txt", 4)
        self.assertEqual(result, "rivi 5.")  # add assertion here


if __name__ == '__main__':
    unittest.main()

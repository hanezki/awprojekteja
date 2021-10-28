import unittest
import testaus.lauseen_muokkaaja.lauseen_muokkaaja as muokkaaja


class TestLauseenMuokkaaja(unittest.TestCase):

    def test_muokkaa_reverses_5_or_longer(self):
        result = muokkaaja.muokkaa("seppo !masa")
        self.assertEqual(result, "Oppes asam!")  # add assertion here

    def test_muokkaa_turns_2_into_uppercase(self):
        result = muokkaaja.muokkaa("seppoli on iloppes")
        self.assertEqual(result, "Iloppes ON seppoli.")


    def test_muokkaa_special_characters_work(self):
        result = muokkaaja.muokkaa("!=123 !! ?? ????????? ()/& SA a?")
        self.assertEqual(result, "321=! !! ?? ????????? ()/& SA A?")


if __name__ == '__main__':
    unittest.main()

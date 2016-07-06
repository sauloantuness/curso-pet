import unittest
from yuri import *

class TestYuri(unittest.TestCase):
    def test_SayHi(self):
        self.assertEqual('hi', hi())

    def test_Fatorial(self):
        self.assertEqual(2, fatorial(2))
        self.assertEqual(6, fatorial(3))
        self.assertEqual(1, fatorial(0))

    def test_ehPar(self):
        self.assertEqual(True, ehPar(0))
        self.assertEqual(True, ehPar(1000))
        self.assertEqual(False, ehPar(1))


if __name__ == '__main__':
    unittest.main()

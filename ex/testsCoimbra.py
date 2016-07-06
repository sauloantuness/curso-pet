import unittest
from coimbra import *

class TestCoimbra(unittest.TestCase):
    def test_SayHi(self):
        self.assertEqual('hi', hi())

    def test_Fatorial(self):
        self.assertEqual(2, fatorial(2))

if __name__ == '__main__':
    unittest.main()

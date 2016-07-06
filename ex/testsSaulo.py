import unittest
from saulo import *

class TestSaulo(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('oi', oi())
    def test_upper2(self):
        self.assertEqual('oi', oi())

if __name__ == '__main__':
    unittest.main()
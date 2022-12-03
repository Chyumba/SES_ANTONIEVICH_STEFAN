from main import count_digits
import unittest

class TestReverse(unittest.TestCase):
    def testCorrect(self):
        self.assertEqual(count_digits("абвгд123АБВГД"),3)

if __name__ =='__main__':
    unittest.main()
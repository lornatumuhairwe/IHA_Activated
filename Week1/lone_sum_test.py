import unittest

from lone_sum import lone_sum

class LoneSumTests(unittest.TestCase):

        def test_number(self):
            self.assertEqual(6, lone_sum(1, 2, 3))
        def test_two_similar_number(self):
            self.assertEqual(3, lone_sum(2, 2, 3))
        def test_three_similar_number(self):
            self.assertEqual(0, lone_sum(3, 3, 3))

if __name__ == '__main__':
        unittest.main()
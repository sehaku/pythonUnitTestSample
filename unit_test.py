import unittest
from tashizan import tashizan
#from firstRepeatChara import findRucurringChara


class Test(unittest.TestCase):
    def test_func(self):
        # tashizan testcase sample
        test_patterns = [
            ([1, 2], 3),
            ([5, 6], 11)
        ]
        for value, expected in test_patterns:
            with self.subTest(value=value):
                self.assertEqual(tashizan(value), expected)
                #self.assertEqual(findRucurringChara(value), expected)


if __name__ == "__main__":
    unittest.main()


'''
# findRecurringChara testcase sample
("ABCA", "A"),
("BCABA", "B"),
("ABC", None),
("DBCABA", "B")
'''

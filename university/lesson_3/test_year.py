import unittest
from func_year import year


class TestYearLeap(unittest.TestCase):
    def test_positive(self):
        res = year(2000)
        self.assertEqual(res, True)
        self.assertTrue(res)

    def test_negative(self):
        res = year(200)
        self.assertEqual(res, False)
        self.assertFalse(res)

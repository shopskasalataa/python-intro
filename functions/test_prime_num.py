from prime_num import *
import unittest


class TestDividers(unittest.TestCase):
    def test_divider(self):
        self.assertEqual(dividers(1), [])
        self.assertEqual(dividers(2), [])
        self.assertEqual(dividers(10), [2, 5])

    def test_negative_dividers(self):
        with self.assertRaises(ValueError):
            dividers(0)
        with self.assertRaises(ValueError):
            dividers(-9)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            dividers([1, 2, 3])


class TestPrimeNum(unittest.TestCase):
    def test_prime_num(self):
        self.assertTrue(prime_num(2))
        self.assertTrue(prime_num(7))

    def test_not_prime_num(self):
        self.assertFalse(prime_num(1))
        self.assertFalse(prime_num(4))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            prime_num([1, 2, 3])


if __name__ == '__main__':
    unittest.main()

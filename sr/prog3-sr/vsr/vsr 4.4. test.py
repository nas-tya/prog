import unittest
from f_n import factorial

class test_factorail(unittest.TestCase):

    def test_f(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(TypeError) as cn:
            factorial(-1)
        self.assertTrue("В качестве аргументов принимаются только натуральные числа" in str(cn.exception))
        with self.assertRaises(TypeError) as cn:
            factorial([2, 3])
        self.assertTrue("В качестве аргументов принимаются только натуральные числа" in str(cn.exception))
        with self.assertRaises(TypeError) as cn:
            factorial((5,6))
        self.assertTrue("В качестве аргументов принимаются только натуральные числа" in str(cn.exception))
        self.assertIs(factorial('2'), 2)
        with self.assertRaises(TypeError) as cn:
            factorial('nnn')
        self.assertTrue("В качестве аргументов принимаются только натуральные числа" in str(cn.exception))            
        self.assertIs(factorial(4.2), 24)
if __name__ == '__main__':
    unittest.main()
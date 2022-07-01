import unittest

import calculate


class TestPrecisionFunc(unittest.TestCase):
    """
    тут мы тестируем функцию, конвертирующую точность
    """

    def test_norm_vals(self):
        self.assertEqual(calculate.convert_precision(0.000001), 6)
        self.assertEqual(calculate.convert_precision(0.0001), 4)

    def test_convertable_inp_value(self):
        self.assertEqual(calculate.convert_precision("0.000001"), 6)

    def test_type_error_raises(self):
        with self.assertRaisesRegex(TypeError, 'wrong argument type'):
            calculate.convert_precision('0.000001a')

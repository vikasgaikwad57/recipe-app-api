"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """test the calc module"""

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        res = calc.substract(15, 10)

        self.assertEqual(res, 5)

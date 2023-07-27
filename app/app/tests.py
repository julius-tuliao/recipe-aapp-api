"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):

        # test the calc module

        def test_add_numbers(self):
            # test adding nuber
            res = calc.add(5,6)

            self.assertEqual(res,11)

        
        def test_substract_numbers(self):
            # test substracting number
            
            res = calc.substract(18,9)

            self.assertEqual(res,9)
              
            

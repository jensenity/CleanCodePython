import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()


import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Jensen', 'Yap', 50000)
        self.emp_2 = Employee('Taeil', 'Kim', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Jensen.Yap@email.com')
        self.assertEqual(self.emp_2.email, 'Taeil.Kim@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Yap@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Kim@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Jensen Yap')
        self.assertEqual(self.emp_2.fullname, 'Taeil Kim')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Yap')
        self.assertEqual(self.emp_2.fullname, 'Jane Kim')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_month_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Yap/May')
            self.assertEqual(schedule, 'Success')


if __name__ == '__main__':
    unittest.main()


###### With Prints ######

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Jensen', 'Yap', 50000)
        self.emp_2 = Employee('Taeil', 'Kim', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Jensen.Yap@email.com')
        self.assertEqual(self.emp_2.email, 'Taeil.Kim@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Yap@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Kim@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Jensen Yap')
        self.assertEqual(self.emp_2.fullname, 'Taeil Kim')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Yap')
        self.assertEqual(self.emp_2.fullname, 'Jane Kim')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()


###### setUpClass and tearDownClass ######

@classmethod
def setUpClass(cls):
    print('setupClass')

@classmethod
def tearDownClass(cls):
    print('teardownClass')


##### Mocking #####
def monthly_schedule(self, month):
    response = requests.get(f'http://company.com/{self.last}/{month}')
    if response.ok:
        return response.text
    else:
        return 'Bad Response!'

def test_month_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Yap/May')
            self.assertEqual(schedule, 'Success')

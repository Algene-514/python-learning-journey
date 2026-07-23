import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.employee01 = Employee('八云蓝',18,70000)
        self.add_value = 10000

    def test_give_default_money(self):
        self.employee01.give_raise()
        self.assertEqual(self.employee01.salary, 75000)

    def test_give_costom_money(self):
        self.employee01.give_raise(self.add_value)
        self.assertEqual(self.employee01.salary, 80000)

if __name__ == '__main__':
    unittest.main()
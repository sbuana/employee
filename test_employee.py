import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print("setUp executed..")
        self.emp_1 = Employee("Satria", "Buana", 15000000)
        self.emp_2 = Employee("Kuswahyuni", "", 6000000)

    def tearDown(self):
        print("tearDown executed..\n")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "satria.buana@company.com")
        self.assertEqual(self.emp_2.email,"kuswahyuni@company.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Satria Buana")
        self.assertEqual(self.emp_2.fullname, "Kuswahyuni")

    def test_salary(self):
        print("test_salary")
        self.assertEqual(self.emp_1.salary, 15000000)
        self.assertEqual(self.emp_2.salary, 6000000)

    def test_applyraise(self):
        print("test_applyraise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.salary, 15750000)
        self.assertEqual(self.emp_2.salary, 6300000)


if __name__ == '__main__':
    unittest.main()

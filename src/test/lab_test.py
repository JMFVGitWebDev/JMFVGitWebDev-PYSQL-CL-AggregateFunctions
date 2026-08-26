import unittest

from src.main.lab import problem1, problem2, problem3, problem4


class LabTest(unittest.TestCase):
    def test_activity_calculate_payroll(self):
        expected_value = 67400.00 + 42500.00 + 99890.99 + 120000 + 55050.50
        result_value = problem1()

        self.assertIsNotNone(result_value)
        self.assertAlmostEqual(expected_value, result_value, places=2)

    def test_activity_count_the_smiths(self):
        expected_value = 2
        result_value = problem2()

        self.assertEqual(expected_value, result_value)

    def test_activity_find_min_salary(self):
        expected = 42500.00
        result = problem3()

        self.assertIsNotNone(result)
        self.assertAlmostEqual(expected, result, places=2)

    def test_activity_find_max_salary(self):
        expected = 120000.00
        result = problem4()

        self.assertIsNotNone(result)
        self.assertAlmostEqual(expected, result, places=2)


if __name__ == "__main__":
    unittest.main()

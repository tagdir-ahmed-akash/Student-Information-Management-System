import unittest
import function  # Ensure this matches the name of your module containing find_stud

class DataBase_test(unittest.TestCase):
    def test_fetch(self):
        expected_name = "Chris Johnson"  # Adjust to match the actual name in your database
        self.assertEqual(function.find_stud(5506104), expected_name)

if __name__ == '__main__':
    unittest.main()

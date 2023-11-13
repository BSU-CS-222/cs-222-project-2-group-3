'''
Testing class
Notes: I personally prefer snake_case over camelCase which is how I changed the tests, if you prefer one naming convention over the other let's go with that
as I would like to be consistent and not make it ugly
'''

import unittest
from Scheduling import CourseScheduler

class TestClassScheduling():
  
    def setUp(self):
        self.scheduler = CourseScheduler()
        self.scheduler.load_courses_from_file('mock_courses.txt')  # Assumption that the method loads courses from a file

    def test_display_all_courses(self):
        # Test to verify if all courses are displayed correctly
        expected_output = [...]  # Expected format and content of the course list
        self.assertEqual(self.scheduler.display_courses(), expected_output)

    def test_enter_number_of_courses(self):
        # Test to verify if the courses entered are valid
        self.assertTrue(self.scheduler.set_course_count(3))  # Assuming that the input was a valid input
        self.assertRaises(ValueError, self.scheduler.set_course_count, -1)  # For Negative numbers
        self.assertRaises(TypeError, self.scheduler.set_course_count, 'a')  # For Non-numeric/string input

    def testEnterCourses(self):
        pass
      
    def testShownSchedule(self): #FR4
        pass


if __name__ == '__main__': #runs tests
    unittest.main()
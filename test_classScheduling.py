'''
Testing class
Notes: I personally prefer snake_case over camelCase which is how I changed the tests, if you prefer one naming convention over the other let's go with that
as I would like to be consistent and not make it ugly

add chck for duplicates

'''

import unittest
from Scheduling import Scheduling

class TestClassScheduling(unittest.TestCase):
  
    def setUp(self):
        self.scheduler = CourseScheduler()
        self.scheduler.load_courses_from_file('mock_courses.txt')  # Assumption that the method loads courses from a file
    
    def test_display_all_courses(self): #FR1
        # Test to verify if all courses are displayed correctly
        expected_output = [...]  # Expected format and content of the course list
        self.assertEqual(self.scheduler.display_courses(), expected_output)

    def test_enter_number_of_courses(self): #FR2
        # Test to verify if the courses entered are valid
        self.assertTrue(self.scheduler.set_course_count(3))  # Assuming that the input was a valid input
        self.assertRaises(ValueError, self.scheduler.set_course_count, -1)  # For Negative numbers
        self.assertRaises(TypeError, self.scheduler.set_course_count, 'a')  # For Non-numeric/string input

    def test_enter_courses(self): #FR3
        # Test to verify if entered courses are stored correctly
        entered_courses = [...]  # List of courses entered by the user
        self.scheduler.enter_courses(entered_courses)
        self.assertEqual(self.scheduler.get_user_courses(), entered_courses)

    def test_shown_schedule(self, course): #FR4
        self.assertEqual(self.scheduler.get_schedule(), "","There is no schedule found")  # checks to see if there is no schedule
        self.scheduler.add_to_schedule(course)
        self.assertEqual(self.scheduler.get_schedule(), course) #makes sure the schedule will show when added

    def check_for_duplicates(self):
        entered_courses = [...]  # List of courses entered by the user
        self.assertFalse(self.scheduler.check_for_duplicates(entered_courses)) #makes sure that the courses shouldn't be the same


if __name__ == '__main__': #runs tests
    unittest.main()

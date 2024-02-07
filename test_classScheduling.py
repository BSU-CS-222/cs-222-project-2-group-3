import unittest
from unittest.mock import patch
from Scheduling import Course, CourseManager, Scheduler

class TestCourse(unittest.TestCase):
    def test_course_creation(self):
        course = Course("CS120", "001", "MWF", "0900", "0950")
        self.assertEqual(course.course_number, "CS120")
        self.assertEqual(course.section, "001")
        self.assertEqual(course.days, "MWF")
        self.assertEqual(course.start_time, "0900")
        self.assertEqual(course.end_time, "0950")

class TestCourseManager(unittest.TestCase):
    def setUp(self):
        self.course_manager = CourseManager()

    def test_load_courses(self):
        # Create a mock courses file
        with open("mock_courses.txt", "w") as file:
            file.write("CS120 001 MWF 0900 0950\n")

        self.course_manager.load_courses("mock_courses.txt")
        self.assertEqual(len(self.course_manager.courses), 1)
    
    def test_find_courses_by_number(self):
        course1 = Course("CS120", "001", "MWF", "0900", "0950")
        course2 = Course("CS120", "002", "TR", "1000", "1050")
        self.course_manager.courses.extend([course1, course2])

        found_courses = self.course_manager.find_courses_by_number("CS120")
        self.assertEqual(len(found_courses), 2)
        self.assertIn(course1, found_courses)
        self.assertIn(course2, found_courses)

    def test_check_time_conflict(self):
        course1 = Course("CS120", "001", "MWF", "0900", "0950")
        course2 = Course("CS121", "002", "MWF", "0930", "1020")
        self.assertTrue(self.course_manager.check_time_conflict(course1, course2))

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = Scheduler()

    def test_generate_non_overlapping_schedule(self):
        # directly added course objects here instead of going through the mock file for brevity sake
        course1 = Course("CS120", "001", "MWF", "0800", "0850")
        course2 = Course("MATH165", "001", "TR", "0900", "0950")
        self.scheduler.course_manager.courses.extend([course1, course2])
        schedule = self.scheduler.generate_non_overlapping_schedule(["CS120", "MATH165"])
        self.assertEqual(len(schedule), 2)
        self.assertIn(course1, schedule)
        self.assertIn(course2, schedule)

    @patch('builtins.input', side_effect=['2', 'CS120', 'MATH165'])
    def test_register_courses(self, mock_input):
        # Set up mock courses in course_manager
        course1 = Course("CS120", "001", "MWF", "0800", "0850")
        course2 = Course("MATH165", "001", "TR", "0900", "0950")
        self.scheduler.course_manager.courses.extend([course1, course2])
        self.scheduler.register_courses()

if __name__ == '__main__':
    unittest.main()

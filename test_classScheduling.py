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

    def test_find_course(self):
        course = Course("CS120", "001", "MWF", "0900", "0950")
        self.course_manager.courses.append(course)

        found_course = self.course_manager.find_course("CS120-001")
        self.assertEqual(found_course, course)

        not_found_course = self.course_manager.find_course("CS121-001")
        self.assertIsNone(not_found_course)

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = Scheduler()

    def test_generate_schedule(self):
        course = Course("CS120", "001", "MWF", "0900", "0950")
        self.scheduler.course_manager.courses.append(course)

        selected_courses = ["CS120-001"]
        schedule = self.scheduler.generate_schedule(selected_courses)

        self.assertEqual(len(schedule), 1)
        self.assertEqual(schedule[0], course)

    @patch('builtins.input', side_effect=['2', 'CS120-001', 'CS121-002'])
    def test_register_courses(self, mock_input):
        self.scheduler.course_manager.load_courses("mock_courses.txt")
        self.scheduler.register_courses()

if __name__ == '__main__':
    unittest.main()
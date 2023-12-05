class Course:
    def __init__(self, course_number, section, days, start_time, end_time):
        self.course_number = course_number
        self.section = section
        self.days = days
        self.start_time = start_time
        self.end_time = end_time

class CourseManager:
    def __init__(self):
        self.courses = []

    def load_courses(self, courses_file="courses.txt"):
        with open(courses_file, "rt") as file:
            for line in file:
                course_parts = line.strip().split()
                if len(course_parts) >= 5:
                    course_key = f"{course_parts[0]}-{course_parts[1]}"
                    # Check if the course is not already in the list before appending
                    if not any(course.course_number == course_key for course in self.courses):
                        course = Course(course_parts[0], course_parts[1], course_parts[2], course_parts[3], course_parts[4])
                        self.courses.append(course)

    def find_course(self, course_key):
        for course in self.courses:
            if f"{course.course_number}-{course.section}" == course_key:
                return course
        return None

class Scheduler:
    def __init__(self):
        self.course_manager = CourseManager()

    def display_available_courses(self):
        print("Available courses:")
        for course in self.course_manager.courses:
            print(f"{course.course_number}-{course.section} | {course.days} | Start: {course.start_time}, End: {course.end_time}")

    def generate_schedule(self, selected_courses):
        schedule = []
        for course_key in selected_courses:
            course = self.course_manager.find_course(course_key)
            if course:
                schedule.append(course)
            else:
                print(f"Course {course_key} not found in the schedule.")
        return schedule

    def register_courses(self):
        n = int(input("Enter how many courses you would like to register for: "))
        selected_courses = []
        for i in range(n):
            course_key = input(f"Enter course code (ex: CS120-001): ")
            selected_courses.append(course_key)

        schedule = self.generate_schedule(selected_courses)

        if schedule:
            print("\nYour Schedule:")
            for course in schedule:
                print(f"Course: {course.course_number} - Section: {course.section}")
                print(f"Days: {course.days} | Time: {course.start_time}-{course.end_time}\n")
        else:
            print("No schedule found for the selected courses.")

# Example usage
scheduler_instance = Scheduler()
scheduler_instance.course_manager.load_courses()
scheduler_instance.display_available_courses()
scheduler_instance.register_courses()
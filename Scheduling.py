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
                    if not any(course.course_number == course_key for course in self.courses):
                        course = Course(course_parts[0], course_parts[1], course_parts[2], course_parts[3], course_parts[4])
                        self.courses.append(course)

    def find_courses_by_number(self, course_number):
        return [course for course in self.courses
                if course.course_number == course_number]

    def check_time_conflict(self, course1, course2):
        days_conflict = any(day in course2.days for day in course1.days)
        time_conflict = not (course1.end_time <= course2.start_time or course1.start_time >= course2.end_time)
        return days_conflict and time_conflict

    def max_offered_courses(self):
        max_courses = {}
        for course in self.courses:
            course_key = f"{course.course_number}"
            if course_key not in max_courses:
                max_courses[course_key] = course

        return list(max_courses.values())

class Scheduler:
    def __init__(self):
        self.course_manager = CourseManager()

    def display_available_courses(self):
        print("Available Courses:".center(60, ' '))
        print("-" * 60)

        unique_courses = sorted(set(course.course_number for course in self.course_manager.courses))
        rows_per_column = 10 
        num_columns = (len(unique_courses) + rows_per_column - 1) // rows_per_column

        for row in range(rows_per_column):
            for col in range(num_columns):
                index = col * rows_per_column + row
                if index < len(unique_courses):
                    print(f"{unique_courses[index]:<20}", end='')
            print()

        print("-" * 60)

    def register_courses(self):
        while True:
            try:
                n = int(input("Enter how many courses you would like to register for: "))
                if n > len(self.course_manager.max_offered_courses()):
                    print("You can't have more courses than " + str(len(self.course_manager.max_offered_courses())))
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")
                
        selected_courses = set()
        while len(selected_courses) < n:
            course_number = input("Enter course number: ").upper()
            if course_number in selected_courses:
                print(f"You already entered {course_number}, Please enter another course.")
            elif not self.course_manager.find_courses_by_number(course_number):
                print(f"Course {course_number} does not exist. Please enter a valid course number.")
            else:
                selected_courses.add(course_number)
        schedule = self.generate_non_overlapping_schedule(list(selected_courses))
        if schedule:
            print("\nYour Schedule:")
            for course in schedule:
                print(f"Course: {course.course_number} - Section: {course.section}")
                print(f"Days: {course.days} | Time: {course.start_time}-{course.end_time}\n")
        else:
            print("No schedule found for the selected courses.")

    def generate_non_overlapping_schedule(self, course_numbers):
        schedule = []
        for number in course_numbers:
            possible_sections = self.course_manager.find_courses_by_number(number)
            for section in possible_sections:
                if all(not self.course_manager.check_time_conflict(section, scheduled_course) for scheduled_course in schedule):
                    schedule.append(section)
                    break
        if len(schedule) == len(course_numbers):
            return schedule
        return None


if __name__ == '__main__':
    scheduler_instance = Scheduler()
    scheduler_instance.course_manager.load_courses()
    scheduler_instance.display_available_courses()
    scheduler_instance.register_courses()
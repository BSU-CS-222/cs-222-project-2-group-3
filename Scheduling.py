class Scheduling:
    def __init__(self, courses_file="courses.txt"):
        self.courses_file = courses_file
        self.course_data = self.read_courses_file()


    # Reads the specified file and returns a list of strings
    def read_courses_file(self):
        with open(self.courses_file, "rt") as file:
            return file.readlines()


    # Takes course_data list, splits it into parts, and creates a dictionary
    def text_file_to_dictionary(self):
        classes_dict = {}
        for line in self.course_data:
            # Over here this function will split each line into parts. So something like (course number, days, times) 
            course_parts = line.strip().split()  # This assumes the file has space-separated values since we know it does
            # Check if the line has the right amount of parts (which in our case is a min of 5
            if len(course_parts) >= 5:
                # Create a unique key for each course (like "CS120-001")
                course_key = f"{course_parts[0]}-{course_parts[1]}"
                # Store course details in the dictionary under the unique key
                classes_dict[course_key] = {
                    "course_number": course_parts[0],
                    "section": course_parts[1],
                    "days": course_parts[2],
                    "start_time": course_parts[3],
                    "end_time": course_parts[4]
                }
        return classes_dict
    

    # Takes list of selected course keys and checks if they exist in the course data dictionary. 
    # If found, they are added to the schedule dictionary.
    def generate_schedule(self, selected_courses):
        schedule = {}
        for course_key in selected_courses:
            # Case-insensitivity and stripping white space
            course_key = course_key.strip().upper()

            # Generate expected course key for comparison
            expected_course_key = f"{course_key.split('-')[0]}-{course_key.split('-')[1]}"

            # Convert the course data to a dictionary
            course_data_dict = self.text_file_to_dictionary()

            if expected_course_key in course_data_dict:  # Check if entered key is in course_data
                schedule[expected_course_key] = course_data_dict[expected_course_key]
            else:
                print(f"Course {course_key} not found in the schedule.")
        return schedule


    # Prints the available courses and prompts user for number of courses to register. 
    def display_available_courses(self):
        print("Available courses:")
        for course_key, details in self.text_file_to_dictionary().items():
            print(f"{course_key} | {details['days']} | Start: {details['start_time']}, End: {details['end_time']}")
            # Formatting for displaying all courses


    # Collects the course keys from the user and generates their schedule.
    def register_courses(self):
        n = int(input("Enter how many courses you would like to register for: "))
        selected_courses = []
        for i in range(n):
            course_key = input(f"Enter course code (ex: CS120-001): ")
            selected_courses.append(course_key)

        schedule = self.generate_schedule(selected_courses)

        if schedule:
            print("\nYour Schedule:")
            for course_key, course in schedule.items():
                print(f"Course: {course['course_number']} - Section: {course['section']}")
                print(f"Days: {course['days']} | Time: {course['start_time']}-{course['end_time']}\n")
        else:
            print("No schedule found for the selected courses.")


# Example usage
scheduling_instance = Scheduling()
scheduling_instance.display_available_courses()
scheduling_instance.register_courses()



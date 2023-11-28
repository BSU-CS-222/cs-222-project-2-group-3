'''
Where all our methods/functions go
'''


class Scheduling:
    def __init__(self, courses_file = "CoursesDemo.txt"):
        self.courses_file = courses_file
        self.course_data = self.read_courses_file()

    def read_courses_file(self):
        with open(self.courses_file, "rt") as file:
            return file.readlines()

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
    

# Example usage
scheduling_instance = Scheduling()
print(scheduling_instance.text_file_to_dictionary())

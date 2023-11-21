'''
Where all our methods/functions go
'''


class Scheduling:
    def __init__(self, courses_file = "CoursesDemo.txt"):
        self.courses = courses_file
        self.fileData = open(self.courses, "rt") # opens file
        self.courseData = self.fileData.readlines() # reads the file
        self.fileData.close()

    def text_file_to_dictionary(self, courseData):
        classes_dict = {}
        for line in courseData: # reads each line in the file
            classes_dict = {"course_number" : line} # this is only returning the last line (problem)

        return classes_dict


# Example usage
scheduling_instance = Scheduling()
print(scheduling_instance.text_file_to_dictionary(scheduling_instance.courseData))

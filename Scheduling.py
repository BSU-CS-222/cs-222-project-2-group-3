'''
Where all our methods/functions go
'''

class CourseScheduler:
    courses = "CoursesDemo.txt"
    fileData = open(courses, "rt")
    courseData = fileData.readlines()
    text_file_to_dictionary()
    fileData.close()

def text_file_to_dictionary():
    classes_dict = {}
    parts = courseData.split(" ")
    course_number = parts[0]
    course_section = parts[1]
    days = days[2]
    start_time = [3]


    classes_dict[] = {
        'course_number': course_number,
        'course_section': course_section,
        'days': days,
        'start_time': start_time,
        'end_time': end_time
    }

    return classes_dict

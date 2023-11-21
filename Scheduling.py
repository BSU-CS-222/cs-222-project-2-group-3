'''
Where all our methods/functions go
'''


class Scheduling:
    courses = "CoursesDemo.txt"
    fileData = open(courses, "rt")
    courseData = fileData.readlines()
    fileData.close()


def text_file_to_dictionary(courseData):
    for line in courseData:
        parts = line.split()
        course_number = parts[0]
        course_section = parts[1]
        days = parts[2]
        start_time = parts[3]
        end_time = parts[4]
        classes_dict = {"course_number": course_number,
                        "course_section": course_section,
                        "days": days,
                        "start_time": start_time,
                        "end_time": end_time
                        }
        print(classes_dict)

    text_file_to_dictionary(courseData)
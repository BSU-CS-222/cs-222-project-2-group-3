'''
Where all our methods/functions go
'''

class CourseScheduler:
    courses = "CoursesDemo.txt"
    fileData = open(courses, "rt")
    courseData = fileData.readlines()
    fileData.close()

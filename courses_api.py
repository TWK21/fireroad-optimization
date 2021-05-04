import requests
import json
import pandas as pd
from random import random

# fetching courses from MIT coursews API
c = requests.get('http://coursews.mit.edu/coursews/?term=2021SP').json()
c2 = requests.get('http://coursews.mit.edu/coursews/?term=2020FA').json()

# initializing data structures
c = c['items']
c2 = c2['items']
ID = []
Units = []
Course = []
Prereqs = []
Semester = []
IsGIR = []
IsHASS = []
Rating = []


# function to add a course
def append_course(id, units, course, prereqs, semester, isGIR, isHASS, rating):
    ID.append(id)
    Units.append(units)
    Course.append(course)
    Prereqs.append(prereqs)
    Semester.append(semester)
    IsGIR.append(isGIR)
    IsHASS.append(isHASS)
    # rating 10 for 15.053 :)
    if id == "15.053":
        Rating.append(10)
    else:
        Rating.append(rating)


# adding HASS and GIR courses
for i in range(1, 9):
    append_course("HASS"+str(i), "12", "0", "",
                  "[\'Fall\', \'Spring\']", "0", "1", round(random()*6 + 4, 1))

for i in range(1, 7):
    append_course("GIR"+str(i), "12", "0", "",
                  "[\'Fall\', \'Spring\']", "1", "0", round(random()*6 + 4, 1))


# possible courses
options = ["6.0001", "6.0002", "6.004", "6.006", "6.009", "6.034", "6.041", "6.042", "6.046",
           "15.276", "15.312", "15.053", "15.075", "15.780", "6.036", "15.093", "15.0251", "15.0341", "15.501", "18.06", "18.03", "18.04", "18.200A", "18.300", "18.600", "18.204", "18.303", "18.330"]

# cleaning data from the API
for course in (c):
    if course['type'] == 'Class':
        if course["id"] in options:
            append_course(course["id"], course['total-units'], course["course"], course['prereqs'],
                          course['semester'], "0", "0", round(random()*6 + 4, 1))
for course in (c2):
    if course['type'] == 'Class':
        if course["id"] in options and "Spring" not in course["semester"]:
            append_course(course["id"], course['total-units'], course["course"], course['prereqs'],
                          course['semester'], "0", "0", round(random()*6 + 4, 1))

# exporting the data to csv
courses = pd.DataFrame({'ID': ID, "Units": Units, "Course": Course,
                        "Prereqs": Prereqs, "Semester": Semester, "IsGIR": IsGIR, "IsHASS": IsHASS, "Rating": Rating})
courses.to_csv("courses.csv")

# add a column for time for scheduling the current semester
# fetch rating from fireroad API or randomly generate utility

# manually remove prerec 14.01 (HASS) and 18.02 (GIR) for 15.0251 for 18.330
# a few missing classes (look for substring from API)

# /recommend/get (GET)
# Takes an optional parameter t indicating the type of recommendation to return. Returns a dictionary of recommendation types mapped to JSON strings indicating the recommended subjects and their rating values.

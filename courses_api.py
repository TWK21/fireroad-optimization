import requests
import json
import pandas as pd

# fetching courses from MIT coursews API
c = requests.get('http://coursews.mit.edu/coursews/?term=2021SP').json()

# initializing data structures
c = c['items']
ID = []
Units = []
Course = []
Prereqs = []
Semester = []

# cleaning data from the API
for course in (c):
    if course['type'] == 'Class':
        ID.append(course["id"])
        Units.append(course['total-units'])
        Prereqs.append(course['prereqs'])
        Semester.append(course['semester'])
        Course.append(course["course"])

# exporting the data to csv
courses = pd.DataFrame({'ID': ID, "Units": Units, "Course": Course,
                        "Prereqs": Prereqs, "Semester": Semester})
datatoexcel = pd.ExcelWriter("test2.xlsx", engine="xlsxwriter")
courses.to_excel(datatoexcel, sheet_name="Sheet1")
datatoexcel.save()


# 1. change xlsx file to csv
# 2. use term 2021FA to add all the coruses only offered in the fall
# 3. fetch rating from fireroad API or randomly generate utility
# 4. add columns for isGIR and isHASS {1,0}
# 5. add a column for time for scheduling the current semester


# /recommend/get (GET)
# Takes an optional parameter t indicating the type of recommendation to return. Returns a dictionary of recommendation types mapped to JSON strings indicating the recommended subjects and their rating values.

import requests
import json

courses = requests.get('http://coursews.mit.edu/coursews/?term=2021SP').json()
math = []
cs = []
business = []

for course in courses["items"]:
    if course["type"] == "Class":
        if "18." in course["id"]:
            math.append(course)
        elif "6." in course["id"]:
            cs.append(course)
        elif "15." in course["id"]:
            business.append(course)

# type, id, total-units, prereqs, semester,
# input: list of classes taken in spring semester
# output: time of the classes

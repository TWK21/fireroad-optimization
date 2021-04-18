import requests

courses = requests.get('http://coursews.mit.edu/coursews/?term=2021SP').text
print(courses)
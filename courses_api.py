import requests

x = requests.get('http://coursews.mit.edu/coursews/?term=2021SP')
print(x)
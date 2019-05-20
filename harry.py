import requests
from pprint import pprint as pp
from bs4 import BeautifulSoup as soup

student_support_services_url = 'https://archive.catalog.ufl.edu/ugrad/1213/Pages/student-support-services.aspx'

response = requests.get(student_support_services_url)
pp(response.text, width=100)

import requests
import re
from pprint import pprint as pp
from bs4 import BeautifulSoup as soup

student_support_services_url = 'https://archive.catalog.ufl.edu/ugrad/1213/Pages/student-support-services.aspx'

with requests.Session() as s:
    response = s.get(student_support_services_url)
    page_soup = soup(response.text, features="lxml")

    regex_pattern = re.search

    # print the first <h1> element
    pp(page_soup.h1)
    # print the first <p> element
    pp(page_soup.p)

    # Todo
    # containers = page_soup.findAll('div', {"class": "s4" + \*\})

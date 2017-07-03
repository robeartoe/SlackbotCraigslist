#In here all settings, all variables can be configured here.
from indeed.indeed import IndeedApi
from config.private import token

slackLA = "#losangeles"
slackNY = "#newyork"

#Indeed Api:
useIndeed = True
api = IndeedApi(token)
JobKeywords = ["Python Internship","Web Developer Internship","Django Internship","python intern","web developer intern"]
cities = ['Los Angeles', 'New York']

#Craigslist Api:
useCraigslist = True
jobCategorys = ['sof', 'jjj']
want_internship = True
resultNumber = 5 #Be careful with this, don't bring back too many results.
Craigslistcities = ['losangeles','newyork']
areas = {'losangeles': ['lac'] , 'newyork': ['mnh','brk','que','brx']}

SLEEP_INTERVAL = 180 * 60 #Three hour Interval
#60 minutes. Change the first number to adjust minutes.

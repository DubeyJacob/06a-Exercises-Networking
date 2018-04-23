#!/usr/bin/env python
'''
This exercise will give you a chance to experiment with making HTTP network requests.
You will first need to install the requests module (using the PyCharm module installer or by following directions here: http://docs.python-requests.org/en/master/user/install/#install)

You will need to accomplish three tasks:
	1. Make a network request against the weather API provided below. Print out the humidity in London as reported by the API
	2. Make a network request against the contact API provided below. Print out Glenna Reichert's email address
	3. Get the text of Dostoyevsky's The Idiot from the Project Gutenberg library. Count and display the total number of stop words (small, common words) in the entire novel. A list of stop words is provided in the stop_words.txt text file

'''
import sys, logging, requests, json, collections
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# -----------------------

'''
weather = 'http://samples.openweathermap.org/data/2.5/weather?q=London\u0026appid=b1b15e88fa797225412429c1c50c122a1'

w = requests.get(weather)
print(w.json())
data = w.json()
for key in data:
	print('{0} -> {1}'.format(key,data[key]))


# Humidity = 81
'''
'''
contacts = 'https://jsonplaceholder.typicode.com/users'

c = requests.get(contacts)
print(c.json())
data = c.json()
for d in data:
	for key in d:
		print('{0} -> {1}'.format(key, d[key]))



# Chaim_McDermott@dana.io
'''

'''
To count the number of times a substring is represented in a string, you can use the string count() method

test_string = "Now is the time for all goodto men to come to the aid of their party."
print(test_string.count('to'))

The count method just finds the exact characters in the string, not taking into account word breaks or capitalization.

You can break a string into words by using the split() method
words = test_string.split()

The Counter class in the collections module has some useful tools.
print(collections.Counter(words)['to'])
print(collections.Counter(words).most_common(5))

If you want to find every word, independent of capitalization, you will need to normalize the case:
words = test_string.lower().split()
'''

stop_words = []
with open('stop_words.txt') as sw:
	stop_words = sw.readlines()
stop_words = [s.strip() for s in stop_words] #remove extra whitespace


the_idiot = 'https://www.gutenberg.org/files/2638/2638-0.txt'
'''
book = requests.get(the_idiot).text
'''

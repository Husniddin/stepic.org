import sys
import requests

url_template = "http://numbersapi.com/{}/math?json=true" 

for number in sys.stdin:
	number = number.rstrip()
	url = url_template.format(number)
	data = requests.get(url).json()
	# print(data)
	if data['found']:
		print('Interesting')
		continue
	print('Boring')
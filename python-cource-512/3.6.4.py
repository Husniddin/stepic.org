import sys
import requests
import json

name = 'husniddinApp'

# client_id = '2936b7a51fac2f811ac9'
# client_secret = 'ab29ed2fd4795be42b3a117c93557d0f'

data = {
	"client_id": client_id,
	"client_secret": client_secret
}

r = requests.post("https://api.artsy.net/api/tokens/xapp_token", data=data)

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}


# инициируем запрос с заголовком
url_template = "https://api.artsy.net/api/artists/{}"
l = []

print('give')

for id in sys.stdin:
	id = id.rstrip()
	if id == 'exit':
		break

	url = url_template.format(id)

	r = requests.get(url, headers=headers)
	j = json.loads(r.text)
	print(j['name'])
	l.append(j['birthday'] + ' ' + j['sortable_name'])

# print(l)
l = sorted(l)
print(l)

for a in l:
	print(a[5:])

import requests

res = requests.get("https://yandex.ru/search/", params={"text": "Stepic"})

print(res.status_code)
print(res.headers)
print(res.headers['Content-Type'])
print(res.url)
# print(res.content)
# print(res.text)

# with open('python.png', 'wb') as image:
	# image.write(res.content)
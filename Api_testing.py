import requests

BASE = 'http://127.0.0.1:5000/'

videos = [{'likes': 10, 'name': 'apex tutorial', 'views': 1020},
            {'likes': 100, 'name': 'python tutorial', 'views': 10000},
            {'likes': 220, 'name': 'cars', 'views': 22}]
for i in range(len(videos)):
    response = requests.put(BASE + 'Video/' + str(i), videos[i])
    print(response.json())

input()
response = requests.get(BASE + 'Video/1')
print(response.json)

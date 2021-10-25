import requests

request = requests.get("https://api.github.com/search/repositories?q=language:python")
data = request.json()

for i in sorted(data["items"], key=lambda x: x["forks"], reverse=True):
    print(f"{i['forks']}. {i['name']}: {i['description']}")


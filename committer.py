import requests
import json

# for i in requests.get('http://localhost:8080/api').content:
    # break



content = requests.get('http://localhost:8080/api')

js = json.loads(content.text)


for i in js:
    print(f"{i['username']} -  {i['pat']}")
    for x in i['repos']:
        print(f"   {x['name']}")
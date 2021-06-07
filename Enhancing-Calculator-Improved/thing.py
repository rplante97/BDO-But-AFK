import requests

value = requests.get("http://bdomarketapi.com/market/NA/items?id=10933", headers={'Connection': 'close'}).json()
for item in value:
    if item["level"] == "6":
        print(item["transactionRecent"])
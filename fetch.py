import requests
import json



url = "http://api.coin360.com/"
proxy = "https://secret-refuge-22081.herokuapp.com/"

response = requests.get(url+"coin/latest?coin=BTC&convert=BTC,ETH,USD")

def jsonPrint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print("\n\n")


jsonPrint(response.json())


print("\n\n")
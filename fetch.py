import requests
import json



url = "http://api.coin360.com/"
proxy = "https://secret-refuge-22081.herokuapp.com/"

response = requests.get(url+"coin/latest?coin=BTC&convert=BTC,ETH,USD")

def json_print(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def json_write(obj):
    # Stores the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    with open("infos.json", "w") as outfile:
        outfile.write(text)

print("\n")


# json_print(response.json())
json_write(response.json())


print("\n")
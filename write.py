import json


json_data = {
    "product":"Python book",
    "overall":"4.0",
    "text":"Nice book"
}

with open("writed_json.json", "w") as jsonFile:
    json.dump(json_data, jsonFile)
    jsonFile.close()
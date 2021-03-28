import json

with open("data.json", "r+") as jsonFile:
    data = json.load(jsonFile)

    data["location"] = "ModifiedPath"
    data["location_mod"] = "Path_NEW"
    jsonFile.seek(0)  # rewind
    json.dump(data, jsonFile, indent=4, sort_keys=True)
    # json.dump(data, jsonFile, indent=4, sort_keys=True)
    jsonFile.truncate() # in case, new data file size is smaller



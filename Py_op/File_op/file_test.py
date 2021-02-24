with open("relayTest.json", "r+") as jsonFile:
    data = json.load(jsonFile)

    data["location"] = "OldPath"
    jsonFile.seek(0)  # rewind
    json.dump(data, jsonFile, indent=4, sort_keys=True)
    jsonFile.truncate() # in case, new data file size is smaller




with open('relay.text', 'r+') as jfile:
    data = json.load(jfile)

    jfile.seek(0)

    jfile.tell()

    json.dump(data, jfile, indent=4, sort_keys=True)

    jfile.truncate()



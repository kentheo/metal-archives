import json


def pprint(parsed):
    print(json.dumps(parsed, indent=4, sort_keys=True))


def writeJsonToFile(data, filePath):
    """
        Write json to file
    """
    with open(filePath, 'w') as f:
        json.dump(data, f)
    print("Successfully wrote all {} data to file {}".format(len(data), filePath))

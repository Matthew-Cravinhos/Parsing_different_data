import json
import yaml #installed in venv

with open('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)

json_file.close()
print(ourjson)
print(ourjson['expires_in'])

print("The access token from JSON is: %s" % ourjson['access_token'])


print("\n\n---")

print(yaml.dump(ourjson))
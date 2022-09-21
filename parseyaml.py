import imp


import json
import yaml

yaml_file = open("myfile.yaml","r") #open the filestream

pythondata = yaml.safe_load(yaml_file) #parse the file stream and python data references

print(pythondata['expires_in'])

print("The access token from YAML is: %s" % pythondata['access_token'])

print("\n\n")
print(json.dumps(pythondata)) #serializes data back out as JSON
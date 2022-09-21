import xml.etree.ElementTree as ET #help library
import re #regular expression engine

xml = ET.parse("myfile.xml") #parse through xml file
root = xml.getroot() #grab the root node

ns = re.match(r'{.*}', root.tag).group(0)
editconf = root.find(f"{ns}edit-config")
defop = editconf.find(f"{ns}default-operation")
testop = editconf.find(f"{ns}test-option")

print("The default-operation contains: %s" % defop.text)
print("The test-option contains: %s" % testop.text)
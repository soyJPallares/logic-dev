import xml.etree.ElementTree as xml
import xml.dom.minidom as md
import json
import os


data: dict = {
    "name": "Jonatan Pallares",
    "age": 48,
    "birth_date": "1977-06-12",
    "dev_languages": ["Python", "Java"]
}


json_file = 'devJPallares.json'
xml_file = 'devJPallares.xml'

# XML

def save_xml():
    root = xml.Element('data')

    for key, value in data.items():
        child = xml.SubElement(root, key)
        
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, 'item').text = str(item)
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)


save_xml()

with open(xml_file) as xml_data:
    xml_string = xml_data.read()

dom = md.parseString(xml_string)
print(dom.toprettyxml(indent="  "))

    # tree = xml.parse(xml_data)
    # root = tree.getroot()

    # print("XML Data:")
    # for child in root:
    #     if child.tag == 'dev_languages':
    #         print(f"{child.tag}: {[item.text for item in child]}")
    #     else:
    #         print(f"{child.tag}: {child.text}")


# JSON

with open(json_file, 'w') as json_data:
    json.dump(data, json_data)

with open(json_file) as json_data:
    print(json.dumps(json.load(json_data), indent=2))


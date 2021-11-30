from xml.etree import ElementTree as ET

"""
XML template for OpenAir requests:
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
		<request API_version="1.0" client="--- client_ver="1.1" namespace="default" key="---">
			<Auth>
				<Login>
					<company>---/company>
					<user>---</user>
					<password>---</password>
				</Login>
			</Auth>
			---
		</request>
"""

def create_wrapper_xml(config, body):
    root = ET.Element(
                "request", 
                attrib={
                    "API_version":"1.0",
                    "client": config['oa_client'], 
                    "client_ver":"1.1", 
                    "namespace":"default", 
                    "key": config['oa_key']
                })
    auth = ET.SubElement(root, "Auth")
    ET.SubElement(auth, "company")
    ET.SubElement(auth, "user")
    ET.SubElement(auth, "password")
    ET.SubElement(root, body)

    return ET.tostring(root)

def create_test_body():
    return ET.Element("Time")

def create_read_body(config):
    read = ET.Element("Read", attrib={
        "type": "",
        "enable_custom": "1", # Does not appear to be a downside to leave this on.
        "filter": "newer-than",
        "field": "updated",
        "limit": "0,1000",
        "method": "all",
        "deleted": "1"
    })
    date = ET.SubElement(read, "Date")
    ET.SubElement(date,"year")
    ET.SubElement(date,"month")
    ET.SubElement(date,"day")
    ET.SubElement(date,"hour")
    ET.SubElement(date,"minute")
    ET.SubElement(date,"second")

    ET.SubElement(read, "_Return")
    # For each field
    return read
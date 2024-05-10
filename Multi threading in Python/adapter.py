"""
	Adapter
	- a structural design pattern that allows objects with incompatible interfaces to collaborate.
"""
import xmltodict
import json

class Application:
    def send_request(self):
        # Simulate an XML data response
        return '<root><data>Hello XML</data></root>'

class Analytic:
    def receive_request(self, json):
        # Analytic now processes JSON data
        print("Processing JSON:", json)

class Adapter:
    def __init__(self, xml_data):
        self.xml_data = xml_data

    def convert_xml_to_json(self):
        # Convert XML string to a Python dictionary and then to a JSON string
        data_dict = xmltodict.parse(self.xml_data)
        return json.dumps(data_dict)

def client_adapter():
    app = Application()
    xml_data = app.send_request()  # Get XML data
    adapter = Adapter(xml_data)
    json_data = adapter.convert_xml_to_json()  # Convert XML to JSON

    analytic = Analytic()
    analytic.receive_request(json_data)  # Process the JSON data

client_adapter()

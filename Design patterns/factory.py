"""
    Factory 
    - Factory is a creational design pattern that provides an interface for creating objects
    in a superclass, but allows subclasses to alter the type of objects that will be created.

    3 Components => 1. creator 2. product 3. client

    creators are deciding what kind of objects should be created. (File, JsonFile, XmlFile)
    products are doing the actual functionality. In the example below, Json ans Xml classes are products.
    client is dealing with client request. (like client function below)
"""


from abc import ABC, abstractmethod

class File(ABC):  # creator
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        #Creates a product and calls its edit method.
        product = self.make()
        result = product.edit(self.file)
        return result


class JsonFile(File):  # creator
    def make(self):
        #Returns a new instance of a Json product.
        return Json()


class XmlFile(File):  # creator
    def make(self):
        #Returns a new instance of an Xml product.
        return Xml()


class Json:  # product
    def edit(self, file):
       #Simulates editing a JSON file.
        return f'Working on {file} json...'


class Xml:  # product
    def edit(self, file):
        #Simulates editing an XML file.
        return f'Working on {file} xml...'


def client(file, format):  # client
    #Factory client function that creates different types of file editors based on the format.
    formats = {
        'json': JsonFile,
        'xml': XmlFile,
    }
    file_class = formats.get(format)
    if file_class is not None:
        editor = file_class(file)
        return editor.call_edit()
    else:
        return f"Error: '{format}' format not supported."

print(client('filename', 'json'))  
print(client('filename', 'xml'))   
print(client('filename', 'yaml'))  

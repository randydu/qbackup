""" 
disk file as task source
""" 

from ..source import Source
from ..json_util import json_serialize

@json_serialize
class FileSource(Source):
    name = ""
    """ single file as task source """
    def __init__(self, name = ""):
        self.name = name

    def __str__(self):
        return self.name
    

@json_serialize
class MultiFileSource(Source):
    """ multiple files as task source """
    names = []
    def __init__(self, names = []):
        self.names = names
    


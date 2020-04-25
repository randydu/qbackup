""" 
disk file as task source
""" 

from .source import Source
from ..json_util import json_serialize

@json_serialize
class File(Source):
    """ single file as task source """
    def __init__(self, name = None):
        self.name = name
    

@json_serialize
class Files(Source):
    """ multiple files as task source """
    def __init__(self, names = None):
        self.names = names
    

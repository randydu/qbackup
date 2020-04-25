""" 
disk file as task source
""" 

from .source import *

class File(Source):
    """ single file as task source """
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

class Files(Source):
    """ multiple files as task source """
    def __init__(self, names):
        self._names = names
    
    @property
    def names(self):
        return self._names


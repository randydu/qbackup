""" disk as task target """

from .target import Target
from ..json_util import json_serialize

class Disk(Target):
    """ local disk as target target """
    pass

@json_serialize
class File(Disk):
    """ target file """
    def __init__(self, name = None):
        super().__init__()
        
        self.name = name

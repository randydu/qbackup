""" disk as task target """

from ..target import Target
from ..json_util import json_serialize

class Disk(Target):
    """ local disk as target target """
    pass

@json_serialize
class FileTarget(Disk):
    name = ""
    """ target file """
    def __init__(self, name = ""):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name
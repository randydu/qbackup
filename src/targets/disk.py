""" disk as task target """

from .target import Target

class Disk(Target):
    """ local disk as target target """
    pass

class File(Disk):
    """ target file """
    def __init__(self, filename):
        super().__init__()
        
        self._name = filename

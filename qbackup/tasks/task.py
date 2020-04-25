"""
Task
"""

from .. import config
from .. import sources
from .. import targets
from ..json_util import MyJSONEncoder, json_deserialize 

        
class Task(object):
    """ Basic unit of job """
    config = None
    source = None
    target = None

    def __init__(self, source = None, target = None):
        self.source = source
        self.target = target

    def to_json(self, pretty:bool = True)->str:
        """ serialize as json string """
        if pretty:
            return MyJSONEncoder(sort_keys=True, indent=4).encode(self)
        else:
            return MyJSONEncoder().encode(self)

    @staticmethod
    def from_json(jstr: str):
        return json_deserialize(jstr)


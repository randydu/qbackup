"""
Task
"""

from .. import config
from .. import sources
from .. import targets
from ..json_util import json_encode, json_decode 

        
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
        return json_encode(self, pretty)

    @staticmethod
    def from_json(jstr: str):
        return json_decode(jstr)

    def run(self):
        """ [sync] execute the task, returns when the task is either done or cancelled """
        from ..runners import Runner
        Runner.getInstance().runTask(self)


"""
Task
"""

from .. import config
from .. import sources
from .. import targets
from ..json_util import json_decode 

from enum import IntEnum
        
class Task(object):
    """ Basic unit of job """
    class Status(IntEnum):
        """ Task status """
        INIT = 0,  # task is inited, not submitted yet
        SUBMITTED = 1, # submitted, before running
        RUNNING = 2, # being executed
        DONE = 3  # finished, either cancelled, success or failure

    class ErrorCode(IntEnum):
        INVALID = 0, # empty / invalid code
        SUCCESS = 1, # no error
        CANCELLED = 2, # cancelled
        ERROR = 3 # error occurs


    _status = Status.INIT
    _ec = ErrorCode.INVALID

    config = None
    source = None
    target = None

    def __init__(self, source = None, target = None):
        self.source = source
        self.target = target

    @property
    def status(self):
        return self._status
    
    @property
    def errcode(self):
        return self._ec


    @staticmethod
    def from_json(jstr: str):
        return json_decode(jstr)

    def run(self):
        """ [sync] execute the task, returns when the task is either done or cancelled """
        from ..runners import Runner
        Runner.getInstance().runTask(self)


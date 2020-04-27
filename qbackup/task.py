"""
Task
"""

from . import config
from . import sources
from . import targets
from .runner import Runner
from .json_util import json_decode, json_encode

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
    _error = None  # task error on failure
    _result = None # task result on success

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

    @property
    def result(self):
        return self._result


    # io
    @staticmethod
    def from_json(jstr: str):
        return json_decode(jstr)

    @staticmethod
    def loadFromFile(fname: str):
        with open(fname, "r") as f:
            jstr = f.read()
        return json_decode(jstr)
    
    def saveToFile(self, fname: str):
        jstr = json_encode(self)
        with open(fname, "w") as f:
            f.write(jstr)

    # run
    def run(self):
        """ [sync] execute the task, returns when the task is either done or cancelled """

        self._error = None
        self._result = None
        
        Runner.getInstance().runTask(self)

    # event listeners
    def onSubmitted(self):
        ''' called when task is submitted to executor engine '''
        self._status = Task.Status.SUBMITTED

    def onRunning(self):
        ''' called when task is being executed by executor engine '''
        self._status = Task.Status.RUNNING

    def onSuccess(self, result):
        ''' called when task is done successfully '''
        self.ErrorCode = Task.ErrorCode.SUCCESS
        self._status = Task.Status.DONE
        self._result = result

    def onError(self, err):
        ''' called when task is done with exception /error '''
        self.ErrorCode = Task.ErrorCode.ERROR
        self._error = err
        self._status = Task.Status.DONE

    def onCancelled(self): 
        ''' called when task is cancelled '''
        self.ErrorCode = Task.ErrorCode.CANCELLED
        self._status = Task.Status.DONE


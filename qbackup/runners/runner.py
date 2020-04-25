from ..tasks import Task
from ..func_util import singleton

from concurrent import futures



@singleton
class Runner(object):
    def __init__(self):
        pass

    def runTask(self, tsk: Task):
        """ runs a task, returns when the task is either done or cancelled """
        pass
    
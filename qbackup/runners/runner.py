from ..tasks import Task
from ..func_util import singleton

from concurrent import futures



@singleton
class Runner(object):
    """ task executor 

        Singleton class
    """

    def __init__(self):
        self._executor = futures.ThreadPoolExecutor(max_workers=2)

    def runTask(self, tsk: Task):
        """ runs a task, returns when the task is done """


        pass
    
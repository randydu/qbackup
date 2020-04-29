
from ...task import Task
from ...runner import Job, runtask
from ...json_util import json_serialize

@json_serialize
class DummyTask(Task):
    ''' dummy task for test '''
    pass

@runtask(DummyTask)
class DummyJob(Job):
    def __call__(self):
        from time import sleep

        total = 5
        for i in range(total):
            sleep(1)
            self._task.progress = (i+1)/total


def _register():
    from ...cmd import registerCmd
    registerCmd('dummy')

_register()

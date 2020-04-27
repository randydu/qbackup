
from ...task import Task
from ...runner import Job, task
from ...func_util import printProgressBar

from ...json_util import json_serialize

@json_serialize
class DummyTask(Task):
    ''' dummy task for test '''
    pass

@task(DummyTask)
class DummyJob(Job):
    def __call__(self):
        from time import sleep

        print("dummy >>>")
        printProgressBar(0, 10, prefix='dummy: ')
        for i in range(10):
            sleep(1)
            printProgressBar(i+1, 10, prefix='dummy')
        print("dummy <<<")

from .runner import Job

from ..json_util import json_serialize

@json_serialize
class DummyJob(Job):
    def __call__(self):
        from time import sleep

        print("dummy >>>")
        for i in range(10):
            sleep(1)
            print(i)
        print("dummy <<<")
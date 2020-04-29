from ...json_util import json_serialize
from ...task import Task
from ...runner import job

@json_serialize
class Hello(Task):
    ''' dummy task for test '''
    who = "World"

@job(Hello)
def sayHello(task):
    print("task:\n", task.to_json())
    print(f"Hello, {task.who}!")


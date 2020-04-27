from unittest import TestCase

from ..task import Task

class Test_Task(TestCase):
    def test_task_create(self):
        tsk = Task()
        self.assertTrue(tsk.source is None)



from unittest import TestCase

from . import dummy

class TestDummy(TestCase):
    def test_dummy(self):
        tsk = dummy.DummyTask()
        jstr = tsk.to_json()
        print(jstr)
        
        tsk1 = dummy.DummyTask.from_json(jstr)
        
        tsk1.run()

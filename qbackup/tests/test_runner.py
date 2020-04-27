from unittest import TestCase

from ..runner import Runner

from ..task import Task
from ..tasks.file_disk import SingleFileDiskCopy
class Test_Runner(TestCase):

    def test_runner_single_instance(self):
        r1 = Runner()
        r2 = Runner()
        r3 = Runner.getInstance()
        self.assertEqual(id(r1), id(r2))
        self.assertEqual(id(r1), id(r3))

    def test_run_single_file_copy(self):
        src = "AAA"
        tgt = "BBB"
        tsk = SingleFileDiskCopy(src, tgt)
        tsk.run()
        self.assertEqual(tsk.status, Task.Status.DONE)

    def test_dummy(self):
        pass
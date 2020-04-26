from unittest import TestCase

from ..runners import Runner
from ..tasks import Task, SingleFileDiskCopy
from ..sources import File as FileSrc
from ..targets import File as FileTgt

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

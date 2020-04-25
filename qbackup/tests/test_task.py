from unittest import TestCase

from ..tasks import Task, SingleFileDiskCopy
from ..sources import File as FileSrc
from ..targets import File as FileTgt

class Test_Task(TestCase):
    def test_task_create(self):
        tsk = Task()
        self.assertTrue(tsk.source is None)

    def test_single_file_disk_copy(self):
        src = "AAA"
        tgt = "BBB"
        tsk = SingleFileDiskCopy(src, tgt)
        self.assertTrue(isinstance(tsk.source, FileSrc))
        self.assertTrue(isinstance(tsk.target, FileTgt))

        jstr = tsk.to_json()

        print(jstr)

        tsk1 = Task.from_json(jstr)
        self.assertTrue(isinstance(tsk1, SingleFileDiskCopy))


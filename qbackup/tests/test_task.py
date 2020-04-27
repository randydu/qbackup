from unittest import TestCase

from ..task import Task
from ..tasks.file_disk import SingleFileDiskCopy
from ..sources.file import FileSource
from ..targets.disk import FileTarget

class Test_Task(TestCase):
    def test_task_create(self):
        tsk = Task()
        self.assertTrue(tsk.source is None)



    def test_single_file_disk_copy(self):
        src = "AAA"
        tgt = "BBB"
        tsk = SingleFileDiskCopy(src, tgt)
        self.assertTrue(isinstance(tsk.source, FileSource))
        self.assertTrue(isinstance(tsk.target, FileTarget))

        jstr = tsk.to_json()

        print(jstr)

        tsk1 = Task.from_json(jstr)
        self.assertTrue(isinstance(tsk1, SingleFileDiskCopy))
        self.assertEqual(tsk.source.name, tsk1.source.name)
        self.assertEqual(tsk.target.name, tsk1.target.name)


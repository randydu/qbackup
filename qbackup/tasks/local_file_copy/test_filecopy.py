from unittest import TestCase

from ...sources.file import FileSource
from ...targets.disk import FileTarget

from .filecopy import *

class TestLocalFileCopy(TestCase):

    def test_single_file_copy(self):
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

        tsk1.run()
        self.assertEqual(tsk1.status, Task.Status.DONE)
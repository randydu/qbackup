""" jobs to do local file copy """ 

from qbackup.job import Job, runtask 
from qbackup.task import Task
from qbackup.sources.file import FileSource
from qbackup.targets.disk import FileTarget

from qbackup.json_util import json_serialize

""" most simple file copy task

  Copy a single file within local disk
"""

def _register():
    from ...cmd import registerCmd
    registerCmd('filecopy')

_register()


@json_serialize
class SingleFileDiskCopy(Task):
    """ single file disk copy in local disk """
    def __init__(self, src: str = "", tgt: str = ""):
        super().__init__()

        self.source = FileSource(src)
        self.target = FileTarget(tgt)


@runtask(SingleFileDiskCopy)
class SingleFileCopyJob(Job):
    def __call__(self): 
        super().__call__()
        
        print(f"copy file {self._task.source.name} => {self._task.target.name}...")


""" jobs to do local file copy """ 

from ...runner import Job, runtask 
from ...task import Task
from ... import sources, targets
from ...json_util import json_serialize

""" most simple file copy task

  Copy a single file within local disk
"""

def _register():
    from ...cmd import registerCmd
    registerCmd('filecopy')

_register()


@json_serialize(version=1)
class SingleFileDiskCopy(Task):
    """ single file disk copy in local disk """
    def __init__(self, src: str = None, tgt: str = None):
        super().__init__()

        self.source = sources.file.FileSource(src)
        self.target = targets.disk.FileTarget(tgt)


@runtask(SingleFileDiskCopy)
class SingleFileCopyJob(Job):
    def __call__(self): 
        super().__call__()
        
        print(f"copy file {self._task.source.name} => {self._task.target.name}...")


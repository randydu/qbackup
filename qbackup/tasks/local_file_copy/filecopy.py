""" jobs to do local file copy """ 

from ...runner import Job, task 
from ...task import Task
from ... import sources, targets
from ...json_util import json_serialize

""" most simple file copy task

  Copy a single file within local disk
"""

@json_serialize(version=1)
class SingleFileDiskCopy(Task):
    """ single file disk copy in local disk """
    def __init__(self, src: str = None, tgt: str = None):
        super().__init__(sources.file.FileSource(src), targets.disk.FileTarget(tgt))


@task(SingleFileDiskCopy)
class SingleFileCopyJob(Job):
    def __call__(self): 
        super().__call__()
        
        print(f"copy file {self._tsk.source.name} => {self._tsk.target.name}...")


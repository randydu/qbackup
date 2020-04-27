""" jobs to do local file copy """ 

from ..runner import Job, task
from ..tasks.file_disk import SingleFileDiskCopy


@task(SingleFileDiskCopy)
class SingleFileCopyJob(Job):
    def __call__(self): 
        super().__call__()
        
        print(f"copy file {self._tsk.source.name} => {self._tsk.target.name}...")



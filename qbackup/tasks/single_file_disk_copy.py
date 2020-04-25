""" most simple file copy task

  Copy a single file within local disk
"""

from .task import Task
from .. import sources, targets


class SingleFileDiskCopy(Task):
    """ single file disk copy in local disk """
    def __init__(self, src, tgt):
        super().__init__(sources.file.File(src), targets.disk.File(tgt))


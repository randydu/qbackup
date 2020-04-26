""" most simple file copy task

  Copy a single file within local disk
"""

from .task import Task
from .. import sources, targets
from ..json_util import json_serialize


@json_serialize(version=1)
class SingleFileDiskCopy(Task):
    """ single file disk copy in local disk """
    def __init__(self, src: str = None, tgt: str = None):
        super().__init__(sources.file.FileSource(src), targets.disk.FileTarget(tgt))




''' global settings ''' 

from .func_util import singleton
from .json_util import json_serialize

@singleton
@json_serialize
class AppConfig:
    """ global settings """
    

@json_serialize
class TaskConfig:
    """ task-specific settings """
    pass
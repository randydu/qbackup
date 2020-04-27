from ..tasks.task import Task
from ..func_util import singleton

from concurrent import futures

@singleton
class Runner(object):
    """ task executor 

        Singleton class
    """

    def __init__(self):
        self._executor = futures.ThreadPoolExecutor(max_workers=2)
        self._mapJob = {}

    def registerJob(self, clsTask, clsJob):
        if clsTask in self._mapJob:
            raise ValueError(f"Duplicated job registration, task: {clsTask.__name__}")
        self._mapJob[clsTask] = clsJob

    def submitJob(self, job):
        return self._executor.submit(job)

    def runTask(self, tsk: Task):
        """ runs a task, returns when the task is done """
        try:
            cls_job = self._mapJob[type(tsk)]
        except KeyError:
            raise ValueError(f"task type ({type(tsk).__name__}) not supported!")
        else:
            return cls_job(tsk).execute()
    
class Job:
    def __init__(self, tsk):
        self._tsk = tsk
        self._future = None

    def __call__(self):
        ''' job being executed 
        
            sub-class must call super().__call__(self) first
        '''
        self._tsk.onRunning()
    
    def cancel(self):
        return self._future.cancel()

    def execute(self, wait = True):
        self._tsk.onSubmitted()
        self._future = Runner.getInstance().submitJob(self)
        self._future.add_done_callback(self._cbDone)
        return self._future.result() if wait else None 

    def _cbDone(self, ft): 
        try:
            self._tsk.onSuccess(ft.result())
        except futures.CancelledError:
            self._tsk.onCancelled()
        except Exception as e:
            self._tsk.onError(e)


    
class task(object):
    """ class decorator to specify which task type to associate 
    
    ex:  
         
         @task(MultiFilesCopy)
         @task(SingleFileCopy)
         class FileCopyJob(Job):
             def __call__(self):
                 pass

    """
    def __init__(self, clsTask):
        self._clsTask = clsTask

    def __call__(self, clsJob):
        Runner.getInstance().registerJob(self._clsTask, clsJob)
        return clsJob


# register all jobs here
from . import filecopy
from .func_util import singleton

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

    def runTask(self, tsk, wait = True):
        """ runs a task, returns when the task is done """
        try:
            cls_job = self._mapJob[type(tsk)]
        except KeyError:
            raise ValueError(f"task type ({type(tsk).__name__}) not supported!")
        else:
            return cls_job(tsk).execute(wait)
    
class Job:
    def __init__(self, task):
        self._task = task
        self._future = None

    def __call__(self):
        ''' job being executed 
        
            sub-class must call super().__call__(self) first
        '''
        self._task.onRunning()
    
    def cancel(self):
        return self._future.cancel()

    def execute(self, wait = True):
        self._task.onSubmitted()
        self._future = Runner.getInstance().submitJob(self)
        self._future.add_done_callback(self._cbDone)
        return self._future.result() if wait else None 

    def _cbDone(self, ft): 
        try:
            self._task.onSuccess(ft.result())
        except futures.CancelledError:
            self._task.onCancelled()
        except Exception as e:
            self._task.onError(e)


    
class runtask(object):
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


def job(clsTask):
    """ function decorator to turn a function into a job class 
    
    @job(clsTask)
    def upload(task):
        ...
    
    """
    
    def toDecorate(f):
        class WrapJob(Job):
            def __call__(self):
                super().__call__()
                f(self._task)
    
        Runner.getInstance().registerJob(clsTask, WrapJob)


    return toDecorate


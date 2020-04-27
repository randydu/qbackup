"""
    function utilities
"""

def _singleton1(cls):
    """ class decorator to implement singleton pattern 
    
        @singleton
        class A: pass

        a1 = A()
        a2 = A.getInstance()

        assert(id(a1) == id(a2))
    
    Advantage:

        the input class is not wrapped by another class

    Side Effects:

        a private field '_singleton' is injected to the input class
    """
    cls._singleton = { "inst": None, "inited": False, "__init__": None }

    def new(c, *args):
        if c._singleton['inst'] is None:
            c._singleton['inst'] = object.__new__(c)
        return c._singleton['inst']
        
    def init(self, *args, **kwargs):
        if not self._singleton['inited']:
            self._singleton['inited'] = True
            self._singleton['__init__'](self, *args, **kwargs) 

    @classmethod
    def getInstance(c):
        return c._singleton['inst'] if c._singleton['inst'] else c()

    cls.__new__ = new
    cls._singleton['__init__'] = cls.__init__
    cls.__init__ = init
    cls.getInstance = getInstance

    return cls


def _singleton2(cls):
    """ class decorator to implement singleton pattern 
    
        @singleton
        class A: pass

        a1 = A()
        a2 = A.getInstance()

        assert(id(a1) == id(a2))
    
    Advantage:

        no field injection to input class

    Side Effects:

        the input class is wrapped by another class
    """
    class SingleCls(cls):
        inst = None
        inited = False

        def __new__(cls, *args):
            if cls.inst is None:
                cls.inst = object.__new__(cls)
            return cls.inst
        
        def __init__(self, *args, **kwargs):
            if not self.inited:
                self.inited = True
                super().__init__(*args, **kwargs) 

        @classmethod
        def getInstance(cls):
            return cls.inst if cls.inst else cls()

    # simulate the name of input class
    SingleCls.__name__ = cls.__name__
    SingleCls.__qualname__ = cls.__qualname__

    return SingleCls


# select which impl to expose?
singleton = _singleton2


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
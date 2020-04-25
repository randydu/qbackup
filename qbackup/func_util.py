"""
    function utilities
"""

def singleton(cls):
    """ class decorator to implement singleton pattern 
    
        @singleton
        class A: pass

        a1 = A()
        a2 = A.getInstance()

        assert(id(a1) == id(a2))
    
    """
    class _singleCls(cls):
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

    return _singleCls
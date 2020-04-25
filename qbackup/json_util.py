

import json



class MyJSONEncoder(json.JSONEncoder):
    types = []

    @classmethod
    def registerClass(cls, new_type):
        cls.types.append(new_type)

    def default(self, obj):
        for t in self.types:
            if isinstance(obj, t):
                r = dict(obj.__dict__)
                r['_cls_'] = type(obj).__module__ + '.' + type(obj).__name__
                return r

        return super().default(obj)

def json_serialize(cls):
    """ class decorator to support json serialization """
    MyJSONEncoder.registerClass(cls)
    return cls
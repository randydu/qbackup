

import json



class MyJSONEncoder(json.JSONEncoder):
    types = {}

    @staticmethod
    def _getTypeKey(typ):
        return f"{typ.__module__}.{typ.__name__}" 

    @classmethod
    def registerClass(cls, new_type):
        key = MyJSONEncoder._getTypeKey(new_type)
        if key in cls.types:
            raise RuntimeError(f"class {key} already registered!")

        cls.types[key] = new_type

    @classmethod
    def resolveClass(cls, cls_key):
        if cls_key in cls.types:
            return cls.types[cls_key]
        raise ValueError(f"class {cls_key} not supported!")


    def default(self, obj):
        mykey = self._getTypeKey(type(obj))

        if mykey in self.types:
            r = dict(obj.__dict__)
            r['_cls_'] = mykey
            return r

        return super().default(obj)


def json_deserialize(jstr):
    """ convert json string to python object """

    def resolve_my_types(dic):
        if '_cls_' in dic:
            key = dic['_cls_']
            typ = MyJSONEncoder.resolveClass(key)

            r = typ()
            return r
        else:
            return dic


            

    return json.loads(jstr, object_hook=resolve_my_types)


def json_serialize(cls):
    """ class decorator to support json serialization """
    MyJSONEncoder.registerClass(cls)
    return cls
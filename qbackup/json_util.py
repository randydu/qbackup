"""
Simple json serialization utility

    Two helper functons (to_json/from_json) added

        @json_serialize
        class A:
            def __init__(self, name):
                self.name = name

        a0 = A('Jack')
        js = a0.to_json()

        a1 = A.from_json(js)
        assert(isinstance(a1, A))
        assert(a0.name == a1.name)

Limit:
------

  the class __init__() must have no mandantary positional parameters

  ex:

    @json_serialize
    class Student:
        def __init__(self, name='', age=18):
            self.name = name
            self.age = age


"""

import json

# the unique key in serialized json object, its value is the full
# identifier of the serialized class
_clsid = '_cls_' 

def _getTypeKey(typ):
    # get a full class identifier from a class type
    return f"{typ.__module__}.{typ.__name__}" 

class _MyJSONEncoder(json.JSONEncoder):
    # customized encoder to support registered classes
    types = {}
    enable_all_fields = False

    @classmethod
    def registerClass(cls, new_type):
        key = _getTypeKey(new_type)
        if key in cls.types:
            raise ValueError(f"class {key} already registered!")

        cls.types[key] = new_type

    @classmethod
    def resolveClass(cls, cls_key):
        if cls_key in cls.types:
            return cls.types[cls_key]
        raise ValueError(f"class {cls_key} not supported!")

    def default(self, obj):
        mykey = _getTypeKey(type(obj))

        if mykey in self.types:
            r = dict(obj.__dict__) if self.enable_all_fields else { k:v for k,v in obj.__dict__.items() if not k.startswith('_') } 
            r[_clsid] = mykey
            return r

        return super().default(obj)


def json_encode(obj, pretty: bool = True, encode_all_fields = False):
    """ convert python object to json string 
    
    if encode_all_fields is true, then all class fields are serialized, otherwise 
    the internal fields (field name starts with '_') are ignored.
    """
    encoder = _MyJSONEncoder(sort_keys=True, indent=4, ensure_ascii=False) if pretty else _MyJSONEncoder(ensure_ascii=False)
    encoder.enable_all_fields = encode_all_fields
    return encoder.encode(obj)


def json_decode(jstr):
    """ convert json string to python object """

    def resolve_my_types(dic):
        # resolve dictionary object to registered json-serializable class instance
        if _clsid not in dic:
            return dic

        key = dic[_clsid]
        typ = _MyJSONEncoder.resolveClass(key)

        r = typ()
        for i in dic:
            if i != _clsid:
                v = dic[i]
                r.__setattr__(i, v if not isinstance(v, dict) else resolve_my_types(v))

        return r

    return json.loads(jstr, object_hook=resolve_my_types)


def json_serialize(cls):
    """ class decorator to support json serialization

       Register class as a known type so it can be serialized and deserialzied properly
    """
    _MyJSONEncoder.registerClass(cls)

    # adds some helper functons
    def to_json(self, pretty:bool = True):
        """ serialize as json string """
        return json_encode(self, pretty)

    @staticmethod
    def from_json(jstr: str):
        return json_decode(jstr)
    
    cls.to_json = to_json
    cls.from_json = from_json

    return cls
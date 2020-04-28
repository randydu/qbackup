from .task import Task


def registerCmd(cmd):
    ''' registers cmd from tasks '''
    print(f"registering {cmd}\r\n")


def run():
    jstr = '{ "_clsid_":"DummyTask" }'
    task = Task.from_json(jstr)
    task.run()

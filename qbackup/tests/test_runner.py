from ..runner import Runner

def test_runner_single_instance():
    r1 = Runner()
    r2 = Runner()
    r3 = Runner.getInstance()
    assert id(r1) == id(r2)
    assert id(r1) == id(r3)

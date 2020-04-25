from unittest import TestCase

from ..runners import Runner

class Test_Runner(TestCase):

    def test_runner_single_instance(self):
        r1 = Runner()
        r2 = Runner()
        r3 = Runner.getInstance()
        self.assertEqual(id(r1), id(r2))
        self.assertEqual(id(r1), id(r3))
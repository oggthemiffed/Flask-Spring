from springpython.config import PythonConfig, Object
from springpython.context import scope
from objects.test_obj import TestObject

__author__ = 'david'

class DemoApplicationContext(PythonConfig):
    def __init__(self):
        super (DemoApplicationContext, self).__init__()

    @Object(scope.SINGLETON, lazy_init=True)
    def TestObject(self):
        to = TestObject()
        to.message = 'Message set by the object context'
        return to

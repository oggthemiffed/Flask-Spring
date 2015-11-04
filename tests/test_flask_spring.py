import sys, os

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/resource"))

from flask import Flask
import pytest
from flask_spring import Spring
from resource.demo_context import DemoApplicationContext

__author__ = 'david'


class TestMainFlaskSpring:
    def setup(self):
        self.app = Flask(__name__)
        self.app.config['SPRING_YAML'] = os.path.realpath(os.path.dirname(__file__) + "/resource/demo.yml")
        self.app.config['SPRING_XML'] = os.path.realpath(os.path.dirname(__file__) + "/resource/demo.xml")
        self.app.config['SPRING_OBJS'] = [DemoApplicationContext()]
        self.spring = Spring(self.app)

    def teardown(self):
        pass

    def setup_class(cls):
        pass

    def teardown_class(cls):
        pass

    def test_create_context(self):
        assert(self.spring._context is None)
        cxt = self.spring.context
        assert(cxt is not None)
        assert(self.spring.context is not None)

    @pytest.mark.parametrize("obj_id, message", [
        ("TestObjectYAML", "This is a test message that is set by spring via YAML config"),
        ("TestObject", "This is a test message that is set by spring via Object context"),
    ])
    def test_load_object_from_config(self, obj_id, message):
        cxt = self.spring.context
        obj = cxt.get_object(obj_id)

        assert(obj is not None)
        assert(obj.message == message)

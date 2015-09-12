from springpython.config import YamlConfig, PyContainerConfig
from springpython.context import ApplicationContext

__author__ = 'david'

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class TestObject(object):
    def __init__(self):
        self.blah = 'Bloop'


class Spring(object):
    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.extensions = getattr(app, "extensions", {})
        app.extensions["spring"] = self

        self._context = None

        app.config['sample'] = TestObject()

        # set any defaults
        app.config.setdefault('SPRING_YAML', 'spring.yml')
        app.config.setdefault('SPRING_XML', None)
        app.config.setdefault('SPRING_OBJS', None)

        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    @property
    def context(self):
        if self._context is None:
            config_loaders = []
            if self.app.config['SPRING_YAML']:
                [config_loaders.append(YamlConfig(config_yaml)) for config_yaml in
                 self.app.config['SPRING_YAML'].split(',')]

            if self.app.config['SPRING_XML']:
                [config_loaders.append(PyContainerConfig(config_xml)) for config_xml in
                 self.app.config['SPRING_XML'].split(',')]

            if self.app.config['SPRING_OBJS']:
                [config_loaders.append(conf_obj) for conf_obj in self.app.config['SPRING_OBJS']]

            self._context = ApplicationContext(config_loaders)

        return self._context

    def teardown(self, exception):
        pass

# ctx = stack.top
#        if hasattr(ctx, 'sqlite3_db'):
#            ctx.sqlite3_db.close()

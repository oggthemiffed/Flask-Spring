from flask import Flask, make_response
from demo_context import DemoApplicationContext
from flask_spring import Spring

__author__ = 'david'

app = Flask(__name__)
app.config['SPRING_YAML'] = 'demo.yml'
app.config['SPRING_OBJS'] = [DemoApplicationContext()]

spring = Spring(app)


@app.route("/")
def show_all():
    cxt = spring.context
    to = cxt.get_object('TestObjectYAML')
    tox = cxt.get_object('TestObjectXML')
    too = cxt.get_object('TestObject')
    message = to.message
    messagexml = tox.message
    messageobj = too.message
    return make_response('YAML: {0} - XML: {1} - OBJ: {2}'.format(message, messagexml, messageobj))


if __name__ == "__main__":
    app.run()

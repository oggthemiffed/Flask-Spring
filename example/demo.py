from flask import Flask, make_response
from demo_context import DemoApplicationContext
from flask_spring import Spring

__author__ = 'david'

app = Flask(__name__)
app.config['SPRING_YAML'] = 'demo.yml'
app.config['SPRING_XML'] = 'demo.xml'
app.config['SPRING_OBJS'] = [DemoApplicationContext()]

spring = Spring(app)


@app.route("/")
def show_all():
    cxt = spring.context
    if app.config['SPRING_YAML']:
        message = (cxt.get_object('TestObjectYAML')).message

    if app.config['SPRING_XML']:
        messagetox = cxt.get_object('TestObjectXML').message

    if app.config['SPRING_OBJS']:
        messageobj = cxt.get_object('TestObject').message

    m ='YAML: {0} - OBJ: {1} - XML: {2}'.format(message if app.config['SPRING_YAML'] is not None else 'Nothing',
                                                 messageobj if app.config['SPRING_OBJS'] is not None else 'Nothing',
                                                 messagetox if app.config['SPRING_XML'] is not None else 'Nothing')

    return make_response(m)


if __name__ == "__main__":
    app.run()

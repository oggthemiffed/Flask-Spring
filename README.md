# Flask-Spring
A flask module to integrate spring framework into a flask application

Build Status: [![Build Status](https://travis-ci.org/oggthemiffed/Flask-Spring.svg?branch=master)](https://travis-ci.org/oggthemiffed/Flask-Spring)
[![PyPI version](https://badge.fury.io/py/flask-spring.svg)](https://badge.fury.io/py/flask-spring)
## Installation

Simply install through pip

```
    pip install flask-spring
```

## Usage

To add the plugin to your project just use the following code (taken from the demo module)

```python
    app = Flask(__name__)
    app.config['SPRING_YAML'] = 'demo.yml'
    app.config['SPRING_XML'] = 'demo.xml'
    app.config['SPRING_OBJS'] = [DemoApplicationContext()]
    
    spring = Spring(app)    
```

###  Configuration

To supply configuration to the plugin then we set the app.config variables as set out below

| Config type | Config Name | Comments                         | Example |
|:-----------:|-------------|----------------------------------|---------|
| YAML        | SPRING_YAML | You can hand in a comma separated list of filenames | demo.yml, demo2.yml|
| XML         | SPRING_XML  |                       *-"-*                         | demo.xml, demo2.xml|
| Objects     | SPRING_OBJS | You can hand in a list of python objects that contain config details | [DemoApplicationContext()] |

Any of the options may be set to None or left if not used.

You must supply one of the following config types:

#### Configuration file format

You can find more information on the file content for all the config file type from the springpython config

| Config Type | Link |
|:-----------:|------|
| YAML        | [YAML Config Docs](http://docs.spring.io/spring-python/1.2.x/sphinx/html/objects-yamlconfig.html)|
| XML         | [XML Config Docs](http://docs.spring.io/spring-python/1.2.x/sphinx/html/objects-xmlconfig.html)|
| Objects     | [Object Config Docs](http://docs.spring.io/spring-python/1.2.x/sphinx/html/objects-pythonconfig.html)|

sudo apt-get -y install python python-virtualenv

virtualenv -p `which python2.7` /opt/pip_env/

source /opt/pip_env/bin/activate

pip install -r  /opt/pip_src/requirements.txt

pip install -U pip setuptools twine wheel

#python setup.py bdist_wheel upload -r https://testpypi.python.org/pypi
#python setup.py sdist upload -r https://testpypi.python.org/pypi

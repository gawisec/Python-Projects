try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Gawisec',
    'url': 'https://github.com/gawisec/Python-Projects/tree/master/projects',
    'author_email': 'gawisec@pm.me',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
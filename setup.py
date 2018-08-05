from os.path import join, dirname
try:
    from setuptools import setup
    from setuptools import find_packages

except ImportError:
    from distutils.core import setup
    from distutils.core import find_packages


def read(fname):
    return open(join(dirname(__file__), fname)).read()

config = {
    'description': '',
    'version': '0.0.1',
    'license': '',
    'url': '',
    'download_url': None,
    'author': '',
    'author_email': '',
    'install_requires': [
    ],
    'packages': [find_packages()],
    'script': [],
    'name': '',
    'long_description': read('README.rst')
}

setup(**config)

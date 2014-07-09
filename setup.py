import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requires = [
    'requests',
    'simplejson',
    'python-dateutil',
    'six'
]

tests_require = [
    'nose',
    'coverage'
]

setup(
    name="decipher",
    version="0.1",
    author="Tristan Wietsma",
    author_email="tristan.wietsma@incontextsolutions.com",
    url="",
    description="A Python client for Decipher",
    packages=["decipher"],
    long_description=read('README.md'),
    setup_requires=['nose'],
    install_requires=install_requires,
    tests_require=tests_require,
    entry_points={
        'console_scripts': [
            'decipher = decipher:cli',
        ],
    }
)

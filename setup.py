from setuptools import setup


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
    name="DecipherAPI",
    version="0.103",
    author="InContext Solutions",
    author_email="quant@incontextsolutions.com",
    url="http://www.incontextsolutions.com/",
    download_url="https://github.com/InContextSolutions/Decipher/tarball/v0.1",
    description="A Python client for Decipher's Beacon API",
    keywords=['Decipher', 'survey'],
    packages=["DecipherAPI"],
    setup_requires=['nose'],
    install_requires=install_requires,
    tests_require=tests_require,
    entry_points={
        'console_scripts': [
            'decipher = DecipherAPI:cli',
        ],
    },
    classifiers=[]
)

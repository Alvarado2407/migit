from setuptools import setup

setup(
    name = 'migit',
    version = '1.0',
    packages = ['migit'],
    entry_points = {
        'console_scripts' : [
            'migit = migit.cli:main'
        ]
    }
)
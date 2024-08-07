from setuptools import setup

setup(
    name='miso',
    version='0.0.1',
    py_modules=['main'],
    entry_points= {
        'console_scripts': [
            'miso=main:main',
        ]
    }
)

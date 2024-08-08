from setuptools import setup, find_packages

setup(
    name='miso',
    version='0.0.2',
    py_modules=["src/main"],
    entry_points= {
        'console_scripts': [
            'miso=src.main:main',
        ]
    }
)

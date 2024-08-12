from setuptools import setup, find_packages

setup(
    name='miso',
    version='0.0.2',
    description= "a cli tool to help optimized workflow by saving frequently used url paths, can also group different urls",
    author= "Junwen Huang",
    author_email= "juntowork@gmail.com",
    packages=find_packages(),
    entry_points= {
        'console_scripts': [
            'miso=src.main:main',
        ]
    }
)

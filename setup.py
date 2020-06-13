from setuptools import setup, find_packages
setup(
    name="polls",
    version="0.1",
    packages=find_packages('src/polls'),
    package_dir={'':'src/polls'}
)
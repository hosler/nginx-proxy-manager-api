from setuptools import setup

setup(
    name='pyngpm',
    version='0.0.1',
    author='Daniel Hosler',
    author_email='danhosler@gmail.com',
    packages=['pyngpm'],
    license='LICENSE.txt',
    description='An API Client for Nginx Proxy Manager',
    long_description=open('README.md').read(),
    install_requires=[
        "requests",
    ],
)

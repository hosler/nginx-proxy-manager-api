from setuptools import setup

setup(
    name='pyngpm',
    version='0.0.1',
    author='Daniel Hosler',
    author_email='danhosler@gmail.com',
    packages=['pyngpm'],
    license='LICENSE',
    description='An API Client for Nginx Proxy Manager',
    install_requires=[
        "requests",
    ],
)

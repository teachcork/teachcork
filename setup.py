from setuptools import setup
from random import randint


setup(name='teachcork',
      version='0.0.1-%d' % (randint(0, 1000), ),
      description='The Tourvox API',
      author='TeachCrok Team',
      author_email='team@teachcork.com',
      packages=[],
      install_requires=[
          'pymongo',
          ])

from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6',]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='BEP',
      version='1.0',
      description='Business Empowerement Platform',
      author='Fabio Alessandro Locati',
      author_email='fabio@locati.cc',
      url='http://bep.locati.cc',
      install_requires=packages,
)


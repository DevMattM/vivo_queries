from setuptools import setup

setup(name= 'vivo_queries',
      packages = ['vivo_queries'],
      version= '0.1',
      description= 'A collection of queries and tools for interacting with VIVO',
      author= 'Naomi Braun',
      author_email= 'naomi.d.braun@gmail.com',
      url= 'http://github.com/naomidb/vivo_queries',
      license= 'Apache License 2.0' ,
      install_requires=[
          'requests==2.18.4',
          'PyYAML==3.12',
          'Jinja2==2.10'],
      )


from setuptools import setup
import glob

setup(
  name='nexus_configurator',
  version='0.2.0',
  description='Manipulate Nexus with Python',
  url='https://github.com/ocadotechnology/nexus-configurator',
  author='Tuskens, stuart-warren',
  install_requires=[
    'requests',
    'pyyaml',
    'jinja2',
  ],
  packages=['nexus'],
  scripts=['bin/nexus_configurator.py'],
  data_files=[('groovy', glob.glob('groovy/*.groovy'))]
)

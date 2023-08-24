from setuptools import find_packages, setup

setup(name='mymodule',
      description='test module for PHY 546',
      url='https://github.com/sbu-python-class/mymodule',
      author='Michael Zingale',
      author_email='michael.zingale@stonybrook.edu',
      license='BSD',
      version="0.0.1",
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'])

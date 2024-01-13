from setuptools import setup, find_packages

setup(name='mymodule',
      description='test module for the SciComp class',
      url='https://github.com/dgerosa',
      author='Davide Gerosa',
      author_email='davide.gerosa@unimib.it',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'])
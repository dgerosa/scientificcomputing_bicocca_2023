from setuptools import setup, find_packages

setup(name='modulescicompclass',
      description='test module for the SciComp class',
      url='https://github.com/dgerosa',
      author='Davide Gerosa',
      author_email='davide.gerosa@unimib.it',
      license='MIT',
      version='0.0.3',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'])
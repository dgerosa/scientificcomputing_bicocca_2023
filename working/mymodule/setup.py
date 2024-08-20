from setuptools import setup, find_packages

setup(name='mymodule', 
      description='show solar system planet orbits', 
      url='https://github.com/Davi9915', 
      author='Davide Tornotti', 
      author_email='d.tornotti@campus.unimib.it', 
      version='0.0.1', 
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib', 'scipy'])
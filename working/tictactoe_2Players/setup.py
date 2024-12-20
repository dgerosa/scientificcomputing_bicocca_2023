from setuptools import setup, find_packages

setup(
    name='tictactoe_2Players',
    version='0.0.2',
    packages=find_packages(),
    author='Matteo Boschini',
    author_email='m.boschini1@campus.unimib.it',
    description='Play Tic-Tac-Toe with your friends!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/m-boschini/scientificcomputing_bicocca_2023/tree/main/working/tictactoe_game',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
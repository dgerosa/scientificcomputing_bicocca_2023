from setuptools import setup, find_packages

setup(
    name="wordleita",
    description="test module the SciComp class",
    url="https://github.com/marcogobbo",
    author="Marco Gobbo",
    author_email="marco.gobbo@gmail.com",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["requests"],
)

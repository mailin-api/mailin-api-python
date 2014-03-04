from setuptools import setup

with open("requirements.txt") as f:
    install_requires = [line.strip() for line in f]

setup(
    name="Sendinblue",
    version="0.0.1",
    py_modules=["Sendinblue"],
    install_requires=install_requires
)

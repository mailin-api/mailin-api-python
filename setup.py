from setuptools import setup

with open("requirements.txt") as f:
    install_requires = [line.strip() for line in f]

setup(
    name="mailin",
    py_modules=["mailin"],
    install_requires=install_requires
)

from setuptools import setup, find_packages

setup(
    name="cnn_binary",
    version="0.1",
    packages=find_packages(include=['scripts', 'scripts.*']),
    include_package_data=True,
)

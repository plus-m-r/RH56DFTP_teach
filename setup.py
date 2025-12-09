from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="plusml-rh56dftp",
    version="0.1.7",
    author="plus-m-r",
    author_email="",
    description="A Python library for communicating with RH56DFTP devices (tactile hand)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/plus-m-r/RH56DFTP_teach",
    packages=find_packages(include=['RH56DFTP', 'Register', 'Register.*']),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pymodbus==3.11.3",
    ],
)

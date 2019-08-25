import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tinylogger',
    version='1.0.0',
    author='frank.zhang',
    author_email='frankzhang02010@gmail.com',
    packages=setuptools.find_packages(),
    url='https://github.com/frankzhangv5/tinylogger-dist',
    license='LICENSE',
    description='An easy use and more powerful android style logging util',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
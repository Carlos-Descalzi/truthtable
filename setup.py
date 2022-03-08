import setuptools
import os

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setuptools.setup(
    name="truthtable",
    version="0.0.1",
    author="Carlos Descalzi",
    author_email="carlos.descalzi@gmail.com",
    description="Displays a truth table based on a boolean expression",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Carlos-Descalzi/truthtable",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["truthtable = truthtable.truthtable:main"]},
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

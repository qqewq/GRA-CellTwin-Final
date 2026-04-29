from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gra-celltwin-final",
    version="0.1.0",
    author="GRA-CellTwin Team",
    description="In silico cell simulator with GRA zeroing for zero-hallucination therapies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qqewq/GRA-CellTwin-Final",
    packages=find_packages(exclude=["tests", "demos"]),
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.24.0",
        "plotly>=5.14.0",
    ],
)

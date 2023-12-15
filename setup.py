import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="battleships-pkg-tkar",
    version="1.0.0",
    author="Tamanna Kar",
    author_email="tkar472@exeter.ac.uk",
    description="Battleships game using Flask API for web interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TKar9901/UoE-Project---Battleships",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating Sytem :: OS Independent",
    ],
    python_requires=">=3.6",
)
    
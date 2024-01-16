import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timeguardian",
    version="0.0.3",
    author="Aldin Cebo",
    author_email="ceboaldin@gmail.com",
    description="TimeGuardian is a package for execution time measurement",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ceboaldin/TimeGuardian",
    packages=setuptools.find_packages(),
    install_requires=[
        'rich',
        'psutil',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
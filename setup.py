from setuptools import setup, find_packages

setup(
    name="minimalboxplot",
    version="1.0.1",
    author="Will Decker",
    author_email="deckerwill7@gmail.com",
    description="Minimal boxplots a la Tufte (2001) p. 125",
    url="https://github.com/w-decker/minimalboxplot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ],
    python_requires='>=3.7',
    install_requires=[
                      'matplotlib',
                      'numpy']

)
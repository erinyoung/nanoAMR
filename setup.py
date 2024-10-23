from setuptools import setup, find_packages

setup(
    name="nanoAMR",
    version="0.0.24298",
    packages=find_packages(), 
    install_requires=[],     
    entry_points={
        'console_scripts': [
            'nanoamr=src.nanoamr:main', 
        ],
    },
    author="Erin Young",
    author_email="eriny@utah.gov",
    description="Find AMR genes on nanopore reads",
    url="https://github.com/erinyoung/nanoAMR",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 4 - Beta ',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics '
    ],
    keywords = [
        "bioinformatics",
        "coverage",
        "visualization",
        "nanopore",
        "antimicrobial resistance",
        "AMR"
    ],
    python_requires=">=3.6, <4",
)

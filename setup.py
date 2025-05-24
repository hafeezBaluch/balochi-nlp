from setuptools import setup, find_packages

# Read the contents of README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="balochi-nlp",
    version="0.1.0",
    author="Hafeez Baloch",
    author_email="hafeezullahhassan2019@gmail.com",
    description="A comprehensive Natural Language Processing toolkit for the Balochi language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hafeezBaluch/balochi-nlp",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "nltk>=3.6.0",
        "scikit-learn>=0.24.0",
        "regex>=2023.0.0",
        "tqdm>=4.65.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "isort>=5.0",
            "flake8>=4.0",
            "mypy>=0.9",
            "tox>=3.24",
        ],
    },
    entry_points={
        "console_scripts": [
            "balochi-nlp=balochi_nlp.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
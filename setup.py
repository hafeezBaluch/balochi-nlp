from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="balochi-nlp",
    version="0.1.0",
    author="PMLS",
    author_email="your.email@example.com",
    description="A comprehensive Natural Language Processing toolkit for the Balochi language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/balochi-nlp",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Balochi",
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
        "regex>=2023.0.0",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "nltk>=3.6.0",
        "scikit-learn>=0.24.0",
        "tqdm>=4.65.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.10.0",
            "pytest-mock>=3.10.0",
            "pytest-asyncio>=0.15.0",
            "black>=21.7b0",
            "flake8>=6.1.0",
            "mypy>=0.910",
            "isort>=5.9.0",
        ],
        "full": [
            "spacy>=3.1.0",
            "transformers>=4.10.0",
            "torch>=1.9.0",
        ],
        "api": [
            "fastapi>=0.68.0",
            "uvicorn>=0.15.0",
            "python-dotenv>=0.19.0",
        ],
    },
)
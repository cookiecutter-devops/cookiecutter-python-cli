"""Package setup"""
import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

requirements = ["click>=8.1.7", "rich>=13.9.4", "rich-click>=1.8.3", "simple-term-menu", "requests","pygments>=2.9.0"]

setuptools.setup(
    name="{{cookiecutter.project_slug}}",
    version="{{cookiecutter.version}}",
    author="{{cookiecutter.author_name}}",
    description="{{cookiecutter.description}}",
    packages=setuptools.find_packages(
        exclude=["dist", "build", "*.egg-info", "tests"]
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "{{cookiecutter.cli_command.strip().lower().replace(' ', '_').replace('-', '_')}} = {{cookiecutter.project_slug}}.app:cli"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
)

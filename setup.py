"""Setup script for Project Nightingale."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="project-nightingale",
    version="1.0.0",
    author="Project Nightingale Team",
    description="A health monitoring and prediction system using wearable data and machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/morningstarxcdcode/Project-Nightingale",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": ["pytest>=7.0.0", "pytest-cov>=4.0.0"],
        "gui": ["tkinter; platform_system != 'Linux'"],
    },
    entry_points={
        "console_scripts": [
            "nightingale=src.main:main",
        ],
        "gui_scripts": [
            "nightingale-gui=gui.main_gui:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
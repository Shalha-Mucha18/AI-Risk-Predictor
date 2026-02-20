from setuptools import setup, find_packages

setup(
    name="vehicle_insurance",
    version="0.0.1",
    author="Shalha_mucha",
    author_email="shalha.mucha@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('requirements.txt') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs]

setup(
    name="metapy",
    version="0.1.4",
    packages=["metapy"],
    include_package_data=True,
    install_requires = install_requires,
    description='metapy',
    long_description=readme,
    author='Rui Hirano',
    license='MIT',
    url='https://ruihirano.github.io/metapy/',
)
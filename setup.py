
from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='My-Awesome-Project',
    url='https://github.com/fahimfarhan/package_demo',
    author='Qazi Fahim Farhan',
    author_email='fahim.farhan@outlook.com',
    # Needed to actually package something
    packages=['measure'],
    # Needed for dependencies
    install_requires=['numpy', 'flask'],
    # *strongly* suggested for sharing
    version='1.0',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)

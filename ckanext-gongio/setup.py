from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-gongio',
    version=version,
    description="Gong.io custom theme",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Nathan Waters',
    author_email='nathan@nathanwaters.com',
    url='http://gong.io',
    license='CC BY-SA 2.5 AU',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.gongio'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
       gongio=ckanext.gongio.plugin:GongioPlugin
    ''',
)

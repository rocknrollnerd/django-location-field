from setuptools import setup
import os

root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

VERSION = __import__('location_field').__version__


setup(
    name='django-location-field',
    version=VERSION,
    description="Location field for Django",
    long_description="This module provides a location field for Django applications.",
    author="Caio Ariede",
    author_email="caio.ariede@gmail.com",
    url="http://github.com/caioariede/django-location-field",
    license="MIT License",
    platforms=["any"],
    packages=['location_field'],
    package_data={'location_field': ['static/location_field/js/*.js',
                                     'templates/location_field/*.html'], },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
)

import os
from setuptools import setup, find_packages

import filemanager


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-webfilemanager',
    version=filemanager.__version__,
    description='Template for reusable django applications.',
    long_description=read('README.rst'),
    license='BSD',
    author='rameez',
    author_email='rameez.arshad@outlook.in',
    url='https://github.com/rameezarshad/django-filemanager',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'django',
    ],
)
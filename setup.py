import os
import platform
import setuptools

try :
	from setuptools import setup,find_packages
except ImportError:
	from distutils.core import setup,find_packages

_VERSION = '0.0.1'

cwd = os.path.dirname(os.path.abspath(__file__))

REQUIRED_PACKAGES = [
	'argparse>=1.1',
    'numpy==1.14.2'
]

setup(name='pyutil',
	packages=['pyutil'],
	version=_VERSION,
	description='Python Util Library',
	install_requires=REQUIRED_PACKAGES,
	classifiers=[
		'Programming Language :: Python :: 3.5',
		'Topic :: Util Functions'
	],
	keywords='util',
	url='',
	author='Andy Tsang',
	author_email='atc1992andy@gmail.com',
	license='Apache License 2.0',
	zip_safe=False)

import os
import platform
import setuptools

_VERSION = '0.0.0'

cwd = os.path.dirname(os.path.abspath(__file__))
on)

REQUIRED_PACKAGES = [
	'argparse>=1.1',
    'dill==0.2.7.1',
	'fire >= 0.1.3',
	'matplotlib >= 2.2.2',
	'psutil >= 5.4.5',
	'requests >= 2.18.4',
	'scikit-image >= 0.13.1',
	'scipy >= 1.0.1',
	'tqdm >= 4.23.4',
	'imutils >= 0.4.6',
	'googledrivedownloader >= 0.2'
]

setup(name='py_util',
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

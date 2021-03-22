from distutils.core import setup
from setuptools import find_packages

setup(
	name = 'django-editable',
	version = '0.1.0',
	author = 'Ash Courchene',
	author_email = 'ash.courchene@gmail.com',
	url = 'http://github.com/Acour83/django-editable',
	license = 'LICENSE.txt',
	description = 'Creates blocks of content that is editable through the frontend with the use of an {% editable %} template tag.',
	packages = find_packages(),
	zip_safe=False,
	include_package_data=True,
)
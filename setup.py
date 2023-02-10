from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in timesheet/__init__.py
from timesheet import __version__ as version

setup(
	name="timesheet",
	version=version,
	description="App to create timesheet for employees",
	author="Novacept",
	author_email="info@novacept.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

from setuptools import setup, find_packages

setup(
    name='mypebble',
    version='1.0.1',
    description="MyPebble website",
    author="SF Software limited t/a Pebble",
    author_email="sysadmin@talktopebble.co.uk",
    url="http://www.mypebble.co.uk",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

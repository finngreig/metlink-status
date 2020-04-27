from setuptools import setup, find_packages

from metlink_status import __version__

with open('README.md', encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name='metlink-status',
    packages=find_packages(),
    version=__version__,
    entry_points={
        'console_scripts': ['metlink-status = metlink_status.cli:main']
    },
    install_requires=[
        'colorama',
        'requests',
        'beautifulsoup4',
        'lxml'
    ],
    description='Python CLI application to check the Metlink Wellington service updates.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='Finn Greig',
    author_email='finn@greig.xyz',
    url='https://github.com/finncodes/metlink-status'
)

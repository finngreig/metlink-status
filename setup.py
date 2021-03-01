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
        'colorama>=0.4.3',
        'requests>=2.23.0',
        'beautifulsoup4>=4.9.0',
        'lxml>=4.5.0'
    ],
    description='Python CLI application to check the Metlink Wellington service updates.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='Finn Greig',
    author_email='finn@greig.xyz',
    url='https://git.sr.ht/~finncodes/metlink-status',
    python_requires='>=3.0',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
    project_urls={
        'Source': 'https://git.sr.ht/~finncodes/metlink-status'
    }
)

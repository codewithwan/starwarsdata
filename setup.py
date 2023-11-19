from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'This Python library interacts with the Star Wars Galaxy API, allowing users to retrieve information about characters, films, and more from the Star Wars universe.'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="starwarsdata",
    version=VERSION,
    author="codewithwan",
    author_email="<deezerxstore@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/codewithwan/starwarsdata',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['data', 'starwars'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)

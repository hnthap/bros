import setuptools


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='bros-mcocr',
    version='0.0.1',
    description='BROS implementation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hnthap/bros.git',
    package_dir={ '': 'bros' },
    packages=setuptools.find_packages(where='bros'),
    python_requires='>=3.9',
)

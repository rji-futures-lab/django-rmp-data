import io
from setuptools import find_packages, setup


with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()


setup(
    name='django-rmp-data',
    version='0.0.1',
    url='https://github.com/rji-futures-lab/django-rmp-data',
    license='MIT',
    maintainer='RJI Futures Lab',
    maintainer_email='gordonj@rjionline.org',
    description='A Django app to extract, refine and publish Risk Management '
                'Plan (RMP) data collected by the U.S. Federal Environment '
                'Protection Agency.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django',
        'django-environ',
        'csvkit',
        'mdbtools',
        'django-postgres-copy',
    ],
)

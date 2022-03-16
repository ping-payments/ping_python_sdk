from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()

setup(
    name='ping_python_sdk',
    version='0.1.0',
    description='Use Ping Payments API to manage merchants, payment orders and payments',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ping Payments developer team',
    author_email='developers@pingpayments.com',
    url='https://www.pingpayments.com/',
    packages=find_packages(),
    install_requires=[
        'jsonpickle~=1.4, >= 1.4.1',
        'requests~=2.25',
    ],
)
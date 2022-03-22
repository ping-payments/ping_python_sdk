from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='ping_python_sdk',
    version='0.1.0',
    description='Use Ping Payments API to manage merchants, payment orders and payments',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ping Payments',
    author_email='developers@pingpayments.com',
    url='https://www.pingpayments.com/',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'jsonpickle~=1.4, >= 1.4.1',
        'requests~=2.25',
    ],
    tests_require=[
         'mypy>=0.910',
         'flake8>=3.9',
         'tox>=3.24'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)

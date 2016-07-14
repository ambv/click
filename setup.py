import ast
import re
import sys
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('click/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


needs_ptr = any(cmd for cmd in sys.argv if cmd in {'ptr', 'pytest', 'test'})
setup_requires = ['pytest-runner'] if needs_ptr else []


setup(
    name='click',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version=version,
    url='http://github.com/pallets/click',
    packages=['click'],
    description='A simple wrapper around optparse for '
                'powerful command line utilities.',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    tests_require=[
        'pytest',
    ],
    setup_requires=setup_requires,
)

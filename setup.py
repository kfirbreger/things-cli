from setuptools import setup


setup(
    name='things-cli',
    version='0.1',
    py_modules=['things_cli',],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        things-cli=things_cli:cli
    ''',
)


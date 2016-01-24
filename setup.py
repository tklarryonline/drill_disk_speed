from setuptools import setup


setup(
    name='drill_disk',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'click',
    ],
    entry_points='''
[console_scripts]
drill_disk=main:main
    '''
)

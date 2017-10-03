from setuptools import setup

setup(
    name='aj-python-junk',
    version='0.0.1',
    description=('If this is in Pypi notify ajarara94'
                 'at googles email service dot commercial'),
    url='https://github.com/alphor/python-junk',
    author='Ahmad Jarara',
    author_email='ajarara94@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Super-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
    keywords='',
    packages=['junk'],
    extras_require={
        'test': ['pytest', 'hypothesis'],
    },
)

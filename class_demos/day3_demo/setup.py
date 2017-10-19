from setuptools import setup


setup(
    name='ackermann',
    description='A package for building and running the ackermann function.',
    package_dir={'': 'src'},
    author='Nicholas Hunt-Walker',
    author_email='nicholas@codefellows.com',
    py_modules=['ackermann'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': [
            'ackermann=ackermann:ackermann'
        ]
    }
)

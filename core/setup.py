from setuptools import setup, find_packages

setup(
    name='jane',
    py_modules=["src"],
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'api=src.api:main'
        ]
    }
)

from setuptools import setup, find_packages

setup(
    name='jane',
    py_modules=["jane"],
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            # 'jane=jane.cli:main',
            'api=jane.api:main'
        ]
    }
)

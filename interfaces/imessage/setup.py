from setuptools import setup, find_packages

setup(
    name='jane-imessage-interface',
    py_modules=["src"],
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            # 'jane=jane.cli:main',
            # 'api=jane.api:main'
        ]
    }
)

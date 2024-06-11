from setuptools import setup, find_packages

setup(
    name='trgpt',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'pyyaml'
    ],
    package_data={
        'trgpt': ['config/config.yaml'],  # Include the config file in the package
    },
    entry_points={
        'console_scripts': [
            'trgpt=trgpt.main:main'
        ]
    },
)

from setuptools import setup, find_packages

setup(
    name='looker_ingestion',
    version='0.0.1',
    description='Extracts adhoc queries from the Looker API to S3',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'looker_sdk'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
        classifiers= [
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ]
)
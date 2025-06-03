from setuptools import setup, find_packages

setup(
    name='polish-sejm-check', # Choose a unique name for your project
    version='0.1.0',
    packages=find_packages(),
    # Add any other dependencies your modules might have (e.g., pandas)
    install_requires=[
        'pandas',
        'requests',
        'asyncio',
        'aiohttp',
        'matplotlib',
        'numpy',
    ],
    # You might need to include data files if your modules use them
    include_package_data=True,
    # package_data={
    #     'your_project_name': ['data/*.csv'],
    # },
)
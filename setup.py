from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='status_page',
    version='0.0.1',
    description='Creates events and incidents on the cashet server',
    long_description=readme,
    author='Arseni',
    author_email='arseni_dudko@epam.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    # entry_points={
    #     'console_scripts': [
    #         'status_page=status_page.cli:main',
    #     ],
    # }
)

from setuptools import setup, find_packages

setup(
    name='hackathonproject',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='My hackathon project',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/oarabile96/package-root',
    author='Oarabile Mokgalagadi',
    author_email='oarabilemokgalagadi@gmail.com'
)

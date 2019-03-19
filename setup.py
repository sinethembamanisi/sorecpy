from setuptools import setup, find_packages

setup(
    name='sorecpy',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/sinethembamanisi/sorecpy.git',
    author='Sinethemba',
    author_email='sinethembamanisi@gmail.com'
)

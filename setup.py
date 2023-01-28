from setuptools import setup

setup(
    name='my_trade',
    version='0.1.0',
    description='My trading library',
    url='https://github.com/RaghavendraGaleppa/MyTrade',
    author='Raghavendra Galeppa',
    author_email='raghavendrar403@gmail.com',
    license='BSD 2-clause',
    packages=['my_trade'],
    install_requires=[
        'numpy',
        'pandas',
        'aiohttp',
    ],


    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
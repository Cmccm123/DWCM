import json
import os
from setuptools import setup




setup(
    name='Dwcm',
    version='0.1.3',
    author="Sunny CM <cm.for.dev@gmail.com>",
    packages=['Dwcm'],
    include_package_data=True,
    license="MIT",
    description="Word Cloud",
    install_requires=['jupyter_dash','dash_html_components','dash'],
    url = 'https://github.com/Cmccm123', 
    download_url = 'https://github.com/Cmccm123/DWCM/archive/refs/tags/D3.tar.gz', 
    keywords = ['D3', 'D3.js', 'Word Cloud','DASH','data visualization'],
    classifiers = [
        'Framework :: Dash',
        'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],    
)

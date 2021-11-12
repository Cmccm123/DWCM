import json
import os
from setuptools import setup


with open('package.json') as f:
    package = json.load(f)

with open(os.path.dirname(os.path.abspath(__file__))+"\\README.txt","r",encoding='utf-8') as fh:
  long_description = fh.read()
package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name='Dwcm',
    version='0.1',
    author=package['author'],
    packages=['Dwcm'],
    include_package_data=True,
    license=package['license'],
    description=package.get('description', package_name),
    install_requires=['jupyter_dash','dash_html_components','dash'],
    keywords = ['D3', 'D3.js', 'Word Cloud','DASH','data visualization'],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers = [
        'Framework :: Dash',
    ],    
)

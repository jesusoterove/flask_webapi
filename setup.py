from setuptools import setup, find_packages
from os import path

requirements = [
    'flask==3.1.0',
]

meta = {}
version_file = path.join(
    path.dirname(__file__),
    'src/flask_webapi',
    '__version__.py'
)

with open(version_file, encoding="utf-8") as f:
    exec(f.read(), meta)

packages = find_packages(where=["src"])
packages = ["flask_webapi"]

print("Flask-WebApi Meta: ", meta)
print("Flask-WebApi Packages: ", packages)

setup(
    name='Flask-WebApi',
    version=meta['__version__'],
    packages=packages,
    package_dir={"flask_webapi": "src/flask_webapi"},
    install_requires=requirements,
    author='Jesus Otero',
    author_email='jesusoterove@gmail.com',
    description='Python Webapi for flask done dotnet style',
    url='https://github.com/jesusoterove/flask_webapi',
    project_urls={
        'Source': 'https://github.com/jesusoterove/flask_webapi',
    },
)

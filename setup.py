from setuptools import setup, find_packages

requirements = [
    'flask==3.1.0',
]

setup(
    name='Flask-WebApi',
    version='1.0.0',
    packages=find_packages(),
    install_requires=requirements,
    author='Jesus Otero',
    author_email='jesusoterove@gmail.com',
    description='Python Webapi for flask done dotnet style',
    url='https://github.com/jesusoterove/flask_webapi',
    project_urls={
        'Source': 'https://github.com/jesusoterove/flask_webapi',
    },
)

from setuptools import setup, find_packages

requirements = [
    'flask==3.1.0',
]

meta = {}
with open("./src/flask_webapi/version.py", encoding="utf-8") as f:
    exec(f.read(), meta)

setup(
    name='Flask-WebApi',
    version=meta['__version__'],
    packages=find_packages(where=["src"]),
    # package_dir={"": "src"},
    install_requires=requirements,
    author='Jesus Otero',
    author_email='jesusoterove@gmail.com',
    description='Python Webapi for flask done dotnet style',
    url='https://github.com/jesusoterove/flask_webapi',
    project_urls={
        'Source': 'https://github.com/jesusoterove/flask_webapi',
    },
)

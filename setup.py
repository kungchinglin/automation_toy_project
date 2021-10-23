from setuptools import setup

# make the README into the long description
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="toy_project",
    version="0.0.1",
    description="Some helper functions",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/kungchinglin/automation_toy_project",
    author="Kung-Ching Lin",
    license="MIT",
    packages=["toy_package"],
    package_dir={"toy_package": "toy_package"},
    # package_data={"mnist_models": ["pretrained_models/*pkl"]},
    install_requires=[
        'mnist>=0.2.2',
        'numpy>=1.21',
        'scikit-learn>=0.24'
    ],
    python_requires=">=3.6",
    zip_safe=False
)

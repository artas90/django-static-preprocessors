from setuptools import setup, find_packages

import static_preprocessors

setup(
    name='django-static-preprocessors',
    version=static_preprocessors.__version__,
    author=static_preprocessors.__author__,
    author_email=static_preprocessors.__contact__,
    description=static_preprocessors.__doc__,
    url=static_preprocessors.__homepage__,
    packages=find_packages(),
    license='MIT',
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)

from gettext import install
from setuptools import setup,find_packages

print(find_packages())

setup(
    name="say_hello24102022",
    version="0.0.2",
    description="Dire bonjour",
    author="Fred",
    email="fred@gmail.com",
    packages=find_packages(),
    install_requires=["requests"],
    license="Apache 2.0",
 classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]    
    )
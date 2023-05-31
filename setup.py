from setuptools import setup, find_packages

setup(
  name="everything",
  author="Dan Rodriguez",
  author_email="hi+everything@dan.ws",
  version="0.0.1",
  description="",
  url="",
  classifiers=[
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
  ],
  packages=find_packages(),
  install_requires=[
    # Core library requirements
    "asyncio",
    "colorama>=0.4",
    "pydantic>=1.8",
    "python-dotenv>=0.19",

    # Required by ChattyLMChannel example
    "transformers",

    # Required by WebChannel example
    "Flask-SocketIO",
    "eventlet",
  ],
)

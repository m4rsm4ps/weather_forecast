from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name="simpweth",
      packages=["simpweth"],
      version="0.0.1",
      author="Mars Maps",
      author_email="m4rsm4ps@gmail.com",
      description="Inaccurate weather forecast library",
      long_description=long_description,
      long_description_content_type="text/markdown",
      )
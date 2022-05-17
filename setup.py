from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simpweth",
    packages=["simpweth"],
    version="0.0.1",
    license='MIT',
    author="Mars Maps",
    author_email="m4rsm4ps@gmail.com",
    description="Inaccurate weather forecast library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m4rsm4ps/weather_forecast",
    keywords=[
        'weather', 'forecast', 'openweater'
    ],
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools"
    ],
    python_requires=">=3.9",
)

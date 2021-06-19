import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="video_toos",
    version="0.0.1",
    author="paulcjh",
    author_email="pcj.hetherington@gmail.com",
    description="Some groovy video tools focused on ML.",
    long_description=long_description,
    url="https://github.com/paulcjh/video_tools",
    # package_dir={"": "video_tools"},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

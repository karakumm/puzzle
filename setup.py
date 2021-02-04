import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puzzle-game-Olena-Karaim",
    version="0.0.1",
    author="Olena Karaim",
    author_email="olena.karaim@ucu.edu.ua",
    description="Puzzle Game is a program that checks if a playing board for logic puzzle is valid.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
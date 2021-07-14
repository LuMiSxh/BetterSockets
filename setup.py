from setuptools import setup, find_packages

classifiers = \
    [
        "Development :: 3 - Alpha",
        "Intended Audience :: Developers ",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python 3"
]

setup(
    name="BetterSockets",
    version="0.0.1a",
    description="Better Python sockets and asyncio streams",
    long_description=open("README.md").read() + "\n\n\n" + open("CHANGELOG.md").read(),
    url="https://github.com/Drageast/BetterSockets",
    author="Luca Michael Schmidt",
    author_email="schmidt.lucamichael@gmail.com",
    license="MIT",
    classifiers=classifiers,
    kewords="sockets",
    packages=find_packages()
)

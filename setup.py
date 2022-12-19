
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolkit',
    version='0.0.3',
    author='srijan',
    author_email='adhyayansrijan1998@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/srijan-stack/toolkit.git',
    project_urls = {
        ""
    },
    license='MIT',
    packages=['toolkit'],
    install_requires=['requests'],
)
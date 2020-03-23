from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


"""
cheat sheet reminder for myself because I'm dumb

python setup.py sdist bdist_wheel
python -m twine upload dist/*
"""


setup(name='vCenterREST',
      version='0.1',
      description='vCenter REST Client',
      url='https://github.com/daveshap/vCenter_REST',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='David Shapiro',
      author_email='daveshap37@gmail.com',
      license='MIT',
      packages=['vCenterREST'],
      zip_safe=False)

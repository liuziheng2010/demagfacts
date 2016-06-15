from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='demagfacts',
      version='0.0.2',
      description=u"Formulas for calculating demagnetiazation factors of FMs",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Julian Irwin",
      author_email='julian.irwin@gmail.com',
      url='https://github.com/julianirwin/demagfacts',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click'
      ],
      entry_points="""
      [console_scripts]
      demagfacts=demagfacts.scripts.cli:cli
      """
      )

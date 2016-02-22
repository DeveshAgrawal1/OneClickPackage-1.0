from setuptools import setup
setup(
  name = 'OneClickPackage',
  packages = ['OneClickPackage'],
  version = '1.0',
  license='MIT',
  download_url='https://github.com/DeveshAgrawal1/OneClickPackage-1.0',
  description = 'One Click Python Package Creator!',
  author = 'Devesh Agrawal',
  author_email = 'dagrawal1096@gmail.com',
  url = 'https://github.com/DeveshAgrawal1/OneClickPackage-1.0',
  keywords = ['python package', 'create package', 'one click'],
  scripts=["src/oneclickpackage.py"],
  install_requires=["wxPython>=2.9.1.1"]
)
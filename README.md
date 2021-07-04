# Makes python package creation easy again!
[![License: MIT](https://img.shields.io/github/license/Souvic/createmypypackage)](https://opensource.org/licenses/MIT)
[![stars](https://img.shields.io/github/stars/Souvic/createmypypackage)]()
[![Github All Releases](https://img.shields.io/github/downloads/huggingface/transformers/total.svg)]()
[![PyPI](https://img.shields.io/pypi/v/createmypypackage)]()
[![python](https://img.shields.io/github/languages/top/Souvic/createmypypackage)]()

[![Build Status](https://scrutinizer-ci.com/g/Souvic/createmypypackage/badges/build.png?b=main)](https://scrutinizer-ci.com/g/Souvic/createmypypackage/build-status/main)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Souvic/package_creator/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/Souvic/package_creator/?branch=main)
[![Release date](https://img.shields.io/github/release-date/Souvic/createmypypackage)]()
[![Latest Stable Version](https://img.shields.io/github/v/release/Souvic/createmypypackage)]()

[![tweet](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FSouvic%2Fcreatemypypackage)]()

### Support me


[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/Souvic)


Most of the packages are simple and a collection of few functions or classes.
We have created a package for that now that can create python packages, upload to github and distribute to pypi all in a single call.
We collect desired packagename, author name and a few info interactively and create the package from a single python file.
You can use multiple python scripts too.
To use multiple scripts give a space seperated list when asked for file locations with main file (the file where all the functions and classes you want user to use is present) at the start.
For simple packaging, one single file is enough.
- [x] Lightweight
- [x] Easiest to use with only one interactive command

> Fun part: This package is also created by running the script located at src/createmypypackage/\_\_init\_\_.py

## Install from PyPi
```
pip3 install createmypypackage
```

## Or Install from main branch
```
pip3 install git+https://github.com/Souvic/createmypypackage.git
```

## Example Usage
### To make a new package and upload to github from a some/one python file(s):
1. Run the below command.
2. Input yes at the first prompt as you will be questioned.
3. Follow the instructions that will appear.
4. Make necessary changes if you have to (e.g. updating README.md file) now on the github repo before submitting to PyPi(by following the upload instruction below)
# One command to create/upload/update them all
```
cmpp
```
#### cmpp is shorthand of _createmypypackage_
#### You can use _createmypypackage_ as the command also with same results

### To update/upload a package to PyPi which already has a GitHub repo:
1. Make all necessary changes in the python files(location: src/packagename/) in the github repo.
2. Run the command (cmpp) as written above to submit to PyPi
3. Input no at the first prompt.
4. Follow the instructions that will appear.
### Set up your $HOME/.pypirc file with the passtoken like this to save twine password to avoid typing username and password everytime [Doc Link](https://twine.readthedocs.io/en/latest/#keyring-support)
Create $HOME/.pypirc and paste the below code replacing only _yourpasstoken
```
[pypi]
  username = __token__
  password = yourpasstoken
```

### Use git store password utility to avoid typing GitHub username and password everytime [Doc Link](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage)
Paste the below code for that with your passtoken and username
```
git credential-store --file ~/.mysecretfilelocation store
protocol=https
host=github.com
username=yourusername
password=passtoken
```
## Important note:
You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content for your README.md


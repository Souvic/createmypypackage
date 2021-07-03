# Makes python package creation easy again!
[![License: MIT](https://img.shields.io/github/license/Souvic/createmypypackage)](https://opensource.org/licenses/MIT)
[![stars](https://img.shields.io/github/stars/Souvic/createmypypackage)]()
[![Github All Releases](https://img.shields.io/github/downloads/huggingface/transformers/total.svg)]()
[![PyPI](https://img.shields.io/pypi/v/createmypypackage)]()
[![Build Status](https://scrutinizer-ci.com/g/Souvic/createmypypackage/badges/build.png?b=main)](https://scrutinizer-ci.com/g/Souvic/createmypypackage/build-status/main)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Souvic/package_creator/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/Souvic/package_creator/?branch=main)
[![Latest Stable Version](https://img.shields.io/github/v/release/Souvic/createmypypackage?include_prereleases)]()
[![Release date](https://img.shields.io/github/release-date/Souvic/createmypypackage)]()
[![python](https://img.shields.io/github/languages/top/Souvic/createmypypackage)]()


### Support me


[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/lukashimsel)


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
### To make a new package:
1. Run the below code to submit to PyPi
2. Input yes at the first prompt.
3. Make necessary changes if you have to (e.g. updating README.md file) now on the github repo before submitting to PyPi(by following the upload instruction below)
# One code to create/upload/update them all
```
python3 -m createmypypackage
```

### To update/upload a package:
1. Make all necessary changes in the python files in the github repo
2. Run the same code as above to submit to PyPi
3. Input no at the first prompt.
4. Input 1 at the second prompt if you are uploading for the first time.
5. Input 2 at the second prompt if you have already submitted once. Change the version in that case to a higher number when prompted.

```
python3 -m createmypypackage 
```
### Use keyring to save twine password to avoid typing username and password everytime [Doc Link](https://twine.readthedocs.io/en/latest/#keyring-support)
Paste the below code for that with your username. Give passtoken when prompted. 
```
keyring set https://upload.pypi.org/legacy/ yourusername
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


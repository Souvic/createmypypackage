# Makes python package creation fun again!

Most of the packages are simple and a collection of few functions or classes.
We have created a package for that now that can create python packages, upload to github and distribute to pypi all in a single call.
We collect desired packagename, author name and a few info interactively and create the package from a single python file.
You can use multiple python scripts too.
To use multiple scripts give a space seperated list when asked for file locations with main file (the file where all the functions and classes you want user to use is present) at the start.
For simple packaging, one single file is enough.

> Fun part: This package is also created by running the script located at src/createmypypackage/\_\_init\_\_.py

## Install from PyPi
```pip3 install createmypypackage```

## Or Install from main branch
```pip3 install git+https://github.com/Souvic/createmypypackage.git```

## Example Usage
### To make a new package:
1. Run the below code to submit to PyPi
2. Input 1 at the first prompt.
## One code to create/upload/update them all
```
python3 -m createmypypackage
```
The above script creates a new package from your python files and uploads to github
Make necessary changes if you have to now on the github repo before submitting to PyPi

### To update/upload a package:
1. Make all necessary changes in the python files in the github repo
2. Run the same code as above to submit to PyPi
3. Input 2 at the first prompt.
4. Input 1 at the second prompt if you are uploading for the first time.
5. Input 2 at the second prompt if you have already submitted once. Change the version in that case to a higher number when prompted.

```
python3 -m createmypypackage 
```
#### Use keyring to save twine password to avoid typing password and username everytime [Doc Link](https://twine.readthedocs.io/en/latest/#keyring-support)

#### Use git store password utility to avoid typing GitHub password and username everytime
Paste the below code for that with your passtoken and username
```
git credential-store --file ~/.mysecretfilelocation store
protocol=https
host=github.com
username=bob
password=passtoken
```

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.


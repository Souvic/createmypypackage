# Makes python package creation easy and fun!

Most of the packages are simple and a collection of few functions or classes.
We have created a package for that now that can create python packages, upload to github and distribute to pypi all in a single call.
We collect desired packagename, author name and a few info interactively and create the package from a single python file.
You can use multiple python scripts too.
To use multiple scripts give a space seperated list when asked for file locations with main file (the file where all the functions and classes you want user to use is present) at the start.
For simple packaging, one single file is enough.

Fun part: This package is also created by running the script located at src/createmypypackage/__init__.py

# Install from PyPi
```pip3 install createmypypackage```

# Or Install from main branch
```pip3 install git+https://github.com/Souvic/createmypypackage.git```

# Example Usage
To make a new package:

```
python -m createmypypackage
```
The above script creates a new package from your python files and uploads to github
Make necessary changes if you have to now on the github repo before submitting to PyPi

To update a package:

```
python -m createmypypackage
```


This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.


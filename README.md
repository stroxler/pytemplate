# Python template package

Includes constants which are aware of the
package directory, clickargs, and click api.
Also has the code for setting up ipython notebook
support that strips output.

# to install

Use pip:
```
pip install -e .
```

# to create a copy

To copy:
```
pytemplate copy-pytemplate --target-directory /some/path/newpackage
```

To install the copy:
```
pip install -e /some/path/newpackage
```

# to add ipython notebook support in the copy

This causes git to strip ipynb output fields, which prevents
your repo from becoming huge when you have ipython notebook demos
```
cd /some/path/newpackage
sh /nb/_setup_git_config.sh
```

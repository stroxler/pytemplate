# Python template package

Includes constants which are aware of the
package directory, clickargs, and click api.
Also has the code for setting up ipython notebook
support that strips output.

## to install

Use pip:
```
pip install -e .
```

## to create a copy

To copy:
```
pytemplate copy-pytemplate --target-directory /some/path/newpackage
```

To install the copy:
```
pip install -e /some/path/newpackage
```

## to add ipython notebook support in the copy

This causes git to strip ipynb output fields, which prevents
your repo from becoming huge when you have ipython notebook demos
```
cd /some/path/newpackage
sh /nb/_setup_git_config.sh
```

## license

### pytemplate packages

BSD license. Feel free to fork, used, modify. If you see
improvements you'd like to make, pull requests are welcome.

### created packages

The license is copied to the packages you create. The copy command will remind
you to delete it / change the owner / swap it out for a license you want your
new package to have. Please do, otherwise your package LICENSE will say that I own
the copyright!

If you want to pull request and add a flag so the license only gets copied
conditionally, please do. I just ran out of time.

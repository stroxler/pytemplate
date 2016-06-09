import re
import os
import shutil

from .constants import PYTEMPLATE_PRJ_DIR


# hacky debugging
VERBOSE = False
def _print(string):
    if VERBOSE:
        print string


def copy_pytemplate(target_directory):
    """
    Copy the pytemplate codebase, replacing the package name as approprate.

    """
    _print("Copying to {}".format(target_directory))
    package_name = os.path.basename(target_directory)
    # copy the codebase
    shutil.copytree(PYTEMPLATE_PRJ_DIR, target_directory,
                    ignore=lambda d, f: ['.git'])
    # remove any lingering temp files
    remove_pyc_and_egg_infos(target_directory)
    # replace pytemplate and PYTEMPLATE as appropriate
    replace_pytemplate(target_directory, package_name)
    # move the package folder
    shutil.move(
        os.path.join(target_directory, 'pytemplate'),
        os.path.join(target_directory, package_name)
    )
    print "Copied to {}".format(target_directory)
    print ("***A BSD license is included***\n"
           "Be sure to change the copyright owner as appropriate\n"
           "for your new package")


def remove_pyc_and_egg_infos(target_directory):
    """
    Remove all the pyc and egg-info files
    """

    def remove_if_pyc_or_egg_info(path):
        if path.endswith('.pyc'):
            _print("removing {}".format(path))
            os.unlink(path)
        elif path.endswith('.egg-info'):
            _print("removing {}".format(path))
            shutil.rmtree(path)

    def remove_in_walk_callback(_, dirname, fnames):
        for f in fnames:
            path = os.path.join(dirname, f)
            remove_if_pyc_or_egg_info(path)

    walk_all(target_directory,
             remove_in_walk_callback,
             None,)


def replace_pytemplate(target_directory, package_name):
    """
    Replace all instances of pytemplate and PYTEMPLATE in the
    full project

    """
    def replace(path):
        _print("replacing pytemplate in {}".format(path))
        replace_pytemplate_in_file(path, 'pytemplate', package_name)
        replace_pytemplate_in_file(path, 'PYTEMPLATE', package_name.upper())

    def remove_in_walk_callback(_, dirname, fnames):
        for f in fnames:
            path = os.path.join(dirname, f)
            if os.path.isfile(path):
                replace(path)

    walk_all(target_directory,
             remove_in_walk_callback,
             None,)


def replace_pytemplate_in_file(filepath, searchfor, replacement):
    """
    Rewrite a file after doing a search-and-replace. See
    `search_and_replace` for details
    """
    _print("Replacing in {}".format(filepath))
    with open(filepath, 'r') as f:
        content = f.read()
    replaced_content = search_and_replace(content, searchfor, replacement)
    with open(filepath, 'w') as f:
        f.write(replaced_content)


def search_and_replace(content, searchfor, replacement):
    """
    Search for a string `searchfor` (which is assumed to be evaluatable as a
    regexp) in a string `content` and replace all instances with `replacement`.
    Return the result.
    """
    rx = re.compile(searchfor)
    return rx.sub(replacement, content)


def walk_all(dirname, func, arg):
    """
    Wrapper around os.path.walk that also walks the top level
    """
    func(arg, dirname, os.listdir(dirname))
    os.path.walk(dirname, func, arg)

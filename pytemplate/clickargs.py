import click


NEW_FILE = click.Path(exists=False)


def target_directory():
    return click.option(
        '--target-directory', '-td', type=NEW_FILE, required=True,
        help="Target directory. The base of this will be the package name"
    )

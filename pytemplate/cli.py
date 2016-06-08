import click


from .copy import copy_pytemplate
import clickargs


@click.group()
def main():
    pass


@main.command('copy-pytemplate')
@clickargs.target_directory()
def _copy_pytemplate(target_directory):
    copy_pytemplate(target_directory)

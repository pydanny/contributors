# -*- coding: utf-8 -*-

from datetime import datetime

import click

from .contributors import get_contribitors
from contributors import __version__


@click.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.version_option(__version__, u'-V', u'--version')
@click.argument(u'repo_names')
@click.option(
    u'-s', u'--since', default=None,
    help=u'Only commits after this date will be returned. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.'
)
@click.option(
    u'-u', u'--until', default=None,
    help=u'Only commits before this date will be returned. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.'
)
def main(repo_names, since, until):
    """Console script for contributors"""
    if since is None:
        since = datetime(2016, 6, 2)
    if until is None:
        until = datetime.now()
    get_contribitors(repo_names, since=since, until=until)


if __name__ == "__main__":
    main()

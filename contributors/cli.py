# -*- coding: utf-8 -*-

from datetime import datetime, tzinfo, timedelta

import click

from .contributors import get_contribitors
from contributors import __version__


class EST(tzinfo):
    def utcoffset(self, dt):
      return timedelta(hours=-8)

    def dst(self, dt):
        return timedelta(0)


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
        since = datetime(2016, 6, 2, tzinfo=EST())
    if until is None:
        until = datetime.now(EST())
    output = get_contribitors(repo_names, since=since, until=until)
    click.echo('\nSaving results to output.rst')
    with open('output.rst', 'w') as f:
        f.write(output)


if __name__ == "__main__":
    main()

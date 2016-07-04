# -*- coding: utf-8 -*-

from __future__ import absolute_import

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
@click.option(
    u'-f', u'--format', default='rst', type=click.Choice(['md', 'rst']),
    help=u'Valid option are "rst" and "md"'
)
@click.option(
    u'-o', u'--output', u'filename', default=None,
    help=u'Output will be written to this file.'
)
def main(repo_names, since, until, format, filename):
    """Console script for contributors"""
    # If the filename is not provided, build a default using the format
    if filename is None:
        filename = 'output.{}'.format(format)
    # If the file extension of the filename provided by the user does
    # not match the format provided, warn the user and continue.
    if filename.rsplit('.', 1)[1] != format:
        click.echo('Warning: file extension does not match output format')
    if since is None:
        since = datetime(2016, 6, 2, tzinfo=EST())
    if until is None:
        until = datetime.now(EST())
    output = get_contribitors(repo_names, since=since, until=until, format=format)
    click.echo('\nSaving results to %s' % filename)
    with open(filename, 'w') as f:
        f.write(output)


if __name__ == "__main__":
    main()

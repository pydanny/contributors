#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_contributors
----------------------------------

Tests for `contributors` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from contributors import contributors
from contributors import cli


class TestContributors(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    def test_command_line_interface_help(self):
        runner = CliRunner()
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '-h, --help             Show this message and exit.' in help_result.output

    @classmethod
    def teardown_class(cls):
        pass

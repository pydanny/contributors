Contributors
============

[![image]]

[![image][1]]

[![Documentation Status]]

[![Updates]]

A command-line script to get all the contributors for one or more GitHub
projects.

-   Free software: Apache Software License 2.0
-   Documentation: <https://contributors.readthedocs.io>.

Usage
-----

1.  Add a [GITHUB\_API\_SECRET]{.title-ref} to your environment
    variables
2.  [pip install contributors]{.title-ref}
3.  Run the command:

``` {.bash}
$ contributors audreyr/cookiecutter,pydanny/cached-property
```

4.  Wait while it processes
5.  Open [output.rst]{.title-ref} in the same directory you ran the
    script.

**Warning:** This may eat up a lot of GitHub bandwidth. If you are
worred about that, do the following to limit the range of search:

``` {.bash}
$ contributors audreyr/cookiecutter,pydanny/cached-property -s 20160602 -u 20160610
```

Examples
--------

-   [PyCon 2016 Cookiecutter sprint contributors]

Credits
-------

This package was created with [Cookiecutter] and the
[audreyr/cookiecutter-pypackage] project template.

  [image]: https://img.shields.io/pypi/v/contributors.svg
  [![image]]: https://pypi.python.org/pypi/contributors
  [1]: https://img.shields.io/travis/pydanny/contributors.svg
  [![image][1]]: https://travis-ci.org/pydanny/contributors
  [Documentation Status]: https://readthedocs.org/projects/contributors/badge/?version=latest
  [![Documentation Status]]: https://contributors.readthedocs.io/en/latest/?badge=latest
  [Updates]: https://pyup.io/repos/github/pydanny/contributors/shield.svg
  [![Updates]]: https://pyup.io/repos/github/pydanny/contributors/
  [PyCon 2016 Cookiecutter sprint contributors]: https://gist.github.com/pydanny/399a431fd91a25620a75a2ce99385566
  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [audreyr/cookiecutter-pypackage]: https://github.com/audreyr/cookiecutter-pypackage
  
  
 Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

### Report Bugs

Report bugs at <https://github.com/pydanny/contributors/issues>.

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in
    troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with \"bug\" is
open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
\"feature\" is open to whoever wants to implement it.

### Write Documentation

Contributors could always use more documentation, whether as part of the
official Contributors docs, in docstrings, or even on the web in blog
posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at
<https://github.com/pydanny/contributors/issues>.

If you are proposing a feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to
    implement.
-   Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

Get Started!
------------

Ready to contribute? Here\'s how to set up [contributors]{.title-ref}
for local development.

1.  Fork the [contributors]{.title-ref} repo on GitHub.

2.  Clone your fork locally:

        $ git clone git@github.com:your_name_here/contributors.git

3.  Install your local copy into a virtualenv. Assuming you have
    virtualenvwrapper installed, this is how you set up your fork for
    local development:

        $ mkvirtualenv contributors
        $ cd contributors/
        $ python setup.py develop

4.  Create a branch for local development:

        $ git checkout -b name-of-your-bugfix-or-feature

    Now you can make your changes locally.

5.  When you\'re done making changes, check that your changes pass
    flake8 and the tests, including testing other Python versions with
    tox:

        $ flake8 contributors tests
        $ python setup.py test or py.test
        $ tox

    To get flake8 and tox, just pip install them into your virtualenv.

6.  Commit your changes and push your branch to GitHub:

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

7.  Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.rst.
3.  The pull request should work for Python 2.6, 2.7, 3.3, 3.4


History
=======

-   Add support for generating output in either markdown or rst with
    `-f` option.

0.3.0 (2016-07-04)
------------------

-   Markdown support
0.2.0 (2016-06-09)
------------------
-   Fix input equality check when rate-limited
-   Allow unauthenticated GitHub API calls
-   Support configurable output filenames


-   Added pull requests and issues
-   Made datetime not niave

0.1.0 (2016-06-09)
------------------

-   First release on PyPI.


# Credits

## Development Leads

  - Daniel Roy Greenfeld \<<pydanny@gmail.com>\>
  - Audrey Roy Greenfeld \<<audreyr@alum.mit.edu>\>

## Contributors

  - Saurabh Kumar / @theskumar
  - Jon Banafato / @jonafato


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

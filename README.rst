===============================
Contributors
===============================


.. image:: https://img.shields.io/pypi/v/contributors.svg
        :target: https://pypi.python.org/pypi/contributors

.. image:: https://img.shields.io/travis/pydanny/contributors.svg
        :target: https://travis-ci.org/pydanny/contributors

.. image:: https://readthedocs.org/projects/contributors/badge/?version=latest
        :target: https://contributors.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/pydanny/contributors/shield.svg
     :target: https://pyup.io/repos/github/pydanny/contributors/
     :alt: Updates

A command-line script to get all the contributors for one or more GitHub projects.


* Free software: Apache Software License 2.0
* Documentation: https://contributors.readthedocs.io.


Usage
--------

1. Add a `GITHUB_API_SECRET` to your environment variables
2. `pip install contributors`
3. Run the command:

.. code-block:: bash

  $ contributors audreyr/cookiecutter,pydanny/cached-property

4. Wait while it processes
5. Open `output.rst` in the same directory you ran the script.

**Warning:** This may eat up a lot of GitHub bandwidth. If you are worred about that, do the following to limit the range of search:

.. code-block:: bash

  $ contributors audreyr/cookiecutter,pydanny/cached-property -s 20160602 -u 20160610

Examples
----------

* `PyCon 2016 Cookiecutter sprint contributors`_


.. _`PyCon 2016 Cookiecutter sprint contributors`: https://gist.github.com/pydanny/399a431fd91a25620a75a2ce99385566

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

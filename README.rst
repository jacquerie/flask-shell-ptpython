======================
 Flask-Shell-PTPython
======================

.. image:: https://travis-ci.org/jacquerie/flask-shell-ptpython.svg?branch=master
    :target: https://travis-ci.org/jacquerie/flask-shell-ptpython


About
=====

Replace the default ``flask shell`` command with a similar one running PTPython.
Inspired by `flask-shell-ipython`_ by `@ei-grad`_.

.. _`flask-shell-ipython`: https://github.com/ei-grad/flask-shell-ipython
.. _`@ei-grad`: https://github.com/ei-grad


Install
=======

``flask-shell-ptpython`` is on PyPI, so all you have to do is:

.. code-block:: console

    $ pip install flask-shell-ptpython


Usage
=====

``flask-shell-ptpython`` hooks itself into Flask through an entry point, so all
you have to do is:

.. code-block:: console

  $ flask shell


Alternatives
============

If you prefer BPython you can use `flask-shell-bpython`_, while if you prefer
IPython you can use `flask-shell-ipython`_.

.. _`flask-shell-bpython`: https://github.com/jacquerie/flask-shell-bpython


Author
======

Jacopo Notarstefano (`@Jaconotar`_)

.. _`@Jaconotar`: https://twitter.com/Jaconotar


License
=======

MIT

django-channels
===============
django-channels is a Django library for sending notifications.
HipChat, Slack, Twitter, and Yo are supported for now.

At a Glance
-----------
After installation and configuration,
you can send notifications to HipChat, Slack, Twitter, or Yo with a following simple code:

.. code-block:: python

   import channels

   channels.send("Sample notification.")

Requirements
------------

Python
^^^^^^
* Python 2.7+
* Python 3.2+
* PyPy
* PyPy3

Django
^^^^^^
* Django 1.7
* Django 1.8
* Django 1.9 (experimental)

Contents
--------
.. toctree::
   :maxdepth: 2

   quickstart
   send
   backends/index
   license

Indices and tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Links
-----
* `Documentation`_
* `GitHub`_

.. _Documentation: http://django-channels.readthedocs.org/
.. _GitHub: https://github.com/ymyzk/django-channels

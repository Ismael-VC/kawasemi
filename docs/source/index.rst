django-channels
===============
django-channels is a Django library for sending notifications.
HipChat and Slack are supported for now.

At a Glance
-----------
After installation and configuration, you can send notifications to HipChat or Slack with a following simple code:

.. code-block:: python

   import channels

   channels.send("Sample notification.")

IMAGE HERE

Contents
--------
.. toctree::
   :maxdepth: 2

   quickstart
   backends/index
   license

Indices and tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

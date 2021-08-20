Installation
============

.. warning::

    The version of ``veros-extra-setups`` *must* match the version of Veros core. When in doubt, you can retrieve the installed Veros version via

    .. code:: bash

      $ veros --version


To install ``veros-extra-setups``, just run

.. code:: bash

    $ pip install veros-extra-setups==<veros-version>


Then, you can use :command:`veros copy-setup` to start using :doc:`the setup files in this package <setup-gallery>`.

.. code:: bash

    $ veros copy-setup --help

.. run-click:: veros.cli.veros:cli
   :args: copy-setup --help

Setup gallery
=============

This page gives an overview of the available model setups. To copy the setup file and additional input files (if applicable) to the current working directory, you can make use of the :command:`veros copy-setup` command.

Example::

   $ veros copy-setup acc_sector


.. note::

   To use the setups below, make sure you have :doc:`veros-extra-setups installed <installation>`.

Idealized configurations
------------------------

+-------------------------------------------+-------------------------------------------+
| :doc:`/setups/acc_sector`                 | :doc:`/setups/fjord`                      |
|                                           |                                           |
| |acc_sector|                              | |fjord|                                   |
+-------------------------------------------+-------------------------------------------+

.. |acc_sector| image:: /_images/gallery/acc_sector.png
  :height: 250px
  :align: middle
  :target: setups/acc_sector.html
  :alt: Steady-state stream function

.. |fjord| image:: /_images/gallery/fjord.png
  :height: 250px
  :align: middle
  :target: setups/fjord.html
  :alt: Steady-state stream function

.. toctree::
   :hidden:

   setups/acc_sector
   setups/fjord

Realistic configurations
------------------------

+--------------------------------------------+-------------------------------------------+
| :doc:`/setups/wave_propagation`            |                                           |
|                                            |                                           |
| |wave-propagation|                         |                                           |
+--------------------------------------------+-------------------------------------------+

.. |wave-propagation| image:: /_images/gallery/wave-propagation.png
   :width: 100%
   :align: middle
   :target: setups/wave_propagation.html
   :alt: Stream function

.. toctree::
   :hidden:

   setups/wave_propagation

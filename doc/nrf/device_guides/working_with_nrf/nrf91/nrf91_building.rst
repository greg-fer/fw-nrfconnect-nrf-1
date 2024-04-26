.. _ug_nrf91_config_build:

Configuring and building with nRF91 Series
##########################################

.. contents::
   :local:
   :depth: 2

Configuring and building applicationg for the nRF91 Series devices follows the processes described in the :ref:`building` section, with several exceptions specific to the nRF91 Series that are listed below.

.. _nrf9160_board_revisions:

nRF9160 DK board revisions
**************************

nRF9160 DK v0.13.0 and earlier has following hardware features missing that are available on later versions of the DK:

* External flash memory
* I/O expander

To build without these features, specify the board revision when building your application.

.. note::
   If you do not specify a board revision, the firmware is built for the default revision (v0.14.0).

To specify the board revision, append it to the board argument when building.
The board revision is printed on the label of your DK, just below the PCA number.
For example, when building a non-secure application for nRF9160 DK v0.9.0, use ``nrf9160dk_nrf9106_ns@0.9.0`` as build target.

See Zephyr's :ref:`zephyr:application_board_version` and :ref:`zephyr:nrf9160dk_additional_hardware` pages for more information.

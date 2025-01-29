.. _tfm_hello_world:

TF-M Hello World
################

.. contents::
   :local:
   :depth: 2

The TF-M Hello World sample is based on Hello World that demonstrates adding Trusted Firmware-M (TF-M) to an application.

Requirements
************

The sample supports the following development kits:

.. table-from-sample-yaml::

Overview
********

This sample uses the Platform Security Architecture (PSA) API to calculate a SHA-256 digest and the TF-M platform read service to read two FICR registers.
The PSA API call is handled by the TF-M secure firmware.

Sample source files
*******************

The sample provides predefined configuration files for typical use cases. You can find the configuration files in the sample directory.

The following files are available:

.. list-table:: Configuration files
   :header-rows: 1

   * - File name
     - Description
   * - :file:`prj.conf`
     - Basic configuration file for the sample.
   * - :file:`prj_bootloaders.conf`
     - Configuration file for enabling bootloaders.

Building and running basic configuration
****************************************

In its basic configuration, the sample uses the :file:`prj.conf` file.

Configuring basic configuration
===============================

|config|

Building basic configuration
============================

.. |sample path| replace:: :file:`samples/tfm/tfm_hello_world`

.. include:: /includes/build_and_run.txt

Testing basic configuration
===========================

After programming the sample, the following output is displayed in the console:

.. code-block:: console

    Hello World! nrf5340dk/nrf5340/cpuapp/ns
    Reading some secure memory that NS is allowed to read
    Approximate IPC overhead us: 65
    FICR->INFO.FLASH: 0x00000400
    Generating random number
    0x03607cef3bdcbbec52edebeb7a0e80756b96d647c82fab068f26d436ff078152
    Example finished successfully!

Dependencies
************

This sample uses the TF-M module that can be found in the following location in the |NCS| folder structure:

* :file:`modules/tee/tfm/`

This sample uses the following libraries:

* :ref:`lib_tfm_ioctl_api`

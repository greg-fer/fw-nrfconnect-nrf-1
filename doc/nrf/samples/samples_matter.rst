.. _matter_samples:

Matter samples
##############

The |NCS| provides several samples showcasing the :ref:`Matter <ug_matter>` protocol.
You can build the samples boards and configure them for different usage scenarios.

All Matter samples are supported by the following devices:

* :ref:`nRF5340 DK <gs_programming_board_names>` (:ref:`nrf5340dk_nrf5340_cpuapp <zephyr:nrf5340dk_nrf5340>`)
* :ref:`nRF52840 DK <gs_programming_board_names>` (:ref:`nrf52840dk_nrf52840 <zephyr:nrf52840dk_nrf52840>`)
* :ref:`nRF21540 DK <gs_programming_board_names>` (:ref:`nrf21540dk_nrf52840 <zephyr:nrf21540dk_nrf52840>`)

The following table lists variants and extensions available out of the box for each Matter sample:

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Variant or extension
      - Light bulb
      - Light switch
      - Door lock
      - Template
    * - FEM support
      - ✔
      - ✔
      - ✔
      - ✔
    * - DFU support
      - ✔
      -
      - ✔
      -
    * - Low power build
      -
      -
      - ✔
      -

See the sample documentation pages for instructions about how to enable these variants and extenstions.

In addition to these samples, check also the :ref:`Thingy:53 Matter weather station <matter_weather_station_app>` application.

.. toctree::
   :maxdepth: 1
   :caption: Subpages
   :glob:

   ../../../samples/matter/*/README

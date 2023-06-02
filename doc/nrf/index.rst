.. _index:

Welcome to the |NCS|!
#####################

The |NCS| is where you begin building low-power wireless applications with Nordic Semiconductor nRF52, nRF53, nRF70, and nRF91 Series devices.

The SDK contains optimized cellular IoT (LTE-M and NB-IoT), Bluetooth® Low Energy, Thread, Zigbee, Wi-Fi®, and Bluetooth mesh stacks, a range of applications, samples, and reference implementations, as well as a full suite of drivers for Nordic Semiconductor's devices.
The |NCS| includes the Zephyr™ real-time operating system (RTOS), which is built for connected low power products.

To access different versions of the |NCS| documentation, use the version drop-down in the top right corner.
A "99" at the end of the version number of this documentation indicates continuous updates on the main branch since the previous major.minor release.

.. raw:: html

   <ul class="grid">
       <li class="grid-item">
	   <a href="introduction.html">
               <span class="grid-icon fa fa-sign-in"></span>
	       <h2>Introductio</h2>
	   </a>
	   <p>Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur,
            adipisci velit.</p>
       </li>
       <li class="grid-item">
	   <a href="getting_started.html">
               <span class="grid-icon fa fa-map-signs"></span>
	       <h2>Ad viam</h2>
	   </a>
	   <p>Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur,
            adipisci velit.</p>
       </li>
       <li class="grid-item">
	   <a href="app_dev.html">
               <span class="grid-icon fa fa-github"></span>
	       <h2>Cave felem</h2>
	   </a>
	   <p>Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur,
            adipisci velit.</p>
       </li>
   </ul>

..

.. toctree::
   :maxdepth: 2
   :caption: SDK installation
   :hidden:

   introduction
   getting_started/recommended_versions
   app_dev/board_support/index
   getting_started/assistant
   getting_started/installing
   getting_started/updating

.. toctree::
   :maxdepth: 2
   :caption: Configuration and building
   :hidden:

   app_dev/build_and_config_system/index
   getting_started/programming
   getting_started/modifying
   app_dev/multi_image/index

.. toctree::
   :maxdepth: 2
   :caption: Testing and optimization
   :hidden:

   getting_started/testing
   app_dev/logging/index
   app_dev/testing_unity_cmock/index
   app_dev/optimizing/index

.. toctree::
   :maxdepth: 2
   :caption: Hardware guides
   :hidden:

   app_dev/pin_control/index
   app_dev/working_with_fem/index
   nrf91
   nrf70
   nrf53
   nrf52
   app_dev/wifi_coex/index

.. toctree::
   :maxdepth: 2
   :caption: SDK components
   :hidden:

   protocols
   applications
   samples
   drivers
   libraries/index
   scripts
   integrations

.. toctree::
   :maxdepth: 2
   :caption: Security
   :hidden:

   security
   app_dev/tfm/index
   app_dev/bootloaders_and_dfu/index
   app_dev/ap_protect/index

.. toctree::
   :maxdepth: 2
   :caption: Releases and maturity
   :hidden:

   dev_model
   release_notes
   known_issues
   software_maturity

.. toctree::
   :maxdepth: 2
   :caption: About this documentation
   :hidden:

   glossary
   documentation/structure
   documentation/build
   documentation/styleguide
   documentation/templates
   documentation/build_process

..   templates/cheat_sheet

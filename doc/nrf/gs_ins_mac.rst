.. _gs_installing_mac:

.. |os| replace:: macOS
.. |installextract| replace:: Extract
.. |system_vars| replace:: \
.. |install_user| replace:: install
.. |tcfolder| replace:: "~/gnuarmemb"
.. |tcfolder_cc| replace:: ``~/gnuarmemb``
.. |bash| replace:: terminal window
.. |envfile| replace:: ``source zephyr/zephyr-env.sh``
.. |rcfile| replace:: ``~/.zephyrrc``
.. |setexport| replace:: export


.. include:: gs_ins_windows.rst
   :start-after: intro_start
   :end-before: intro_end



.. _gs_installing_tools_mac:

Installing the required tools
*****************************

To install the required tools, follow the :ref:`zephyr:mac_requirements` section of Zephyr's Getting Started Guide.
Install Homebrew and install the required tools using the ``brew`` command line tool.


.. _gs_installing_toolchain_mac:

.. include:: gs_ins_windows.rst
   :start-after: toolchain_start
   :end-before: toolchain_end



.. _cloning_the_repositories_mac:

.. include:: gs_ins_windows.rst
   :start-after: cloning_start
   :end-before: cloning_end



.. _additional_deps_mac:

.. include:: gs_ins_windows.rst
   :start-after: add_deps_start
   :end-before: add_deps_end



.. _installing_ses_mac:

.. include:: gs_ins_windows.rst
   :start-after: installing_ses_start
   :end-before: installing_ses_end



.. _build_environment_mac:

.. include:: gs_ins_windows.rst
   :start-after: buildenv_start
   :end-before: buildenv_end

.. _additional_mac_setup:

Setting up executables on macOS
===============================

If you start SES on macOS by running the file :file:`bin/emStudio`, make sure to complete the following steps:

1. Specify the path to all executables under :guilabel:`Tools` -> :guilabel:`Options` (in the :guilabel:`nRF Connect` tab).
   The global PATH on macOS is used only when :ref:`using the command line environment <build_environment_cli_mac>`. 

    .. figure:: images/ses_options.png
         :alt: nRF Connect SDK options in SES on Windows

         nRF Connect SDK options in SES (Windows)
   
   Use this section to change the SES environment settings later as well.

#. Specify the path to the west tool as additional CMake option, replacing *path_to_west* with the path to the west executable (for example, ``/usr/local/bin/west``):

    .. parsed-literal::
       :class: highlight

       -DWEST=\ *path_to_west*

.. _build_environment_cli_mac:

.. include:: gs_ins_windows.rst
   :start-after: buildenv_cli_start
   :end-before: buildenv_cli_end

.. note::
    
    Unlike on Windows and Linux, the global PATH variable is used to find executables on macOS only if you start SES from the command line.   
    If you get an error that a tool or command cannot be found, first make sure that the tool is installed.
    If it is installed, add its location to the PATH variable.
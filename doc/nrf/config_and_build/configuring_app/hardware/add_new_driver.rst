.. _add_new_driver:

Adding new drivers
##################

.. contents::
   :local:
   :depth: 2

To add a new driver to an application in the nRF Connect SDK, complete the following steps:

.. rst-class:: numbered-step

Add the driver files
********************

The |NCS| includes a variety of :ref:`drivers` that are used in its samples and applications.
You can use one of them

First, create the new driver that will provide code for communication with the sensor.
Use the two existing |NCS| drivers as an example.

Create a DTS binding
Configure sensor through DTS
Include sensor in the application

1. **Enable necessary Kconfigs in the application**: You need to enable your custom driver and application-defined syscalls in the `prj.conf` file. For example:

```bash
CONFIG_CUSTOM_DRIVER=y
CONFIG_APPLICATION_DEFINED_SYSCALL=y
```
[source](https://academy.nordicsemi.com/courses/nrf-connect-sdk-intermediate/lessons/lesson-7-device-driver-model/topic/exercise-1-13/#Exercise-steps)

2. **Add the driver directory as a Zephyr module**: You can add the driver directory as a Zephyr module into the project in the `CMakeLists.txt` file. For example:

```bash
list(APPEND EXTRA_ZEPHYR_MODULES
  ${CMAKE_CURRENT_SOURCE_DIR}/custom_driver
  )
```

3. **Add a custom driver initialization priority**: You need to add a custom driver initialization priority in the `Kconfig` file of your driver. For example:

```bash
config DRIVER_INIT_PRIORITY
	int "Init priority"
	default 71
	help
```

Select the new sensor

Useful |NCS| modules
********************

If your application uses buttons and LEDs, you can use the :ref:`Common Application Framework <caf_overview>` with its :ref:`button <caf_buttons>` and :ref:`LED <caf_leds>` modules to gather input from them and drive them using application events.

Implementation examples
***********************

Check the following driver implementation examples:

* :ref:`nrf_desktop` application describes how to :ref:`add a new motion sensor to the project <porting_guide_adding_sensor>`.
* `nRF Connect SDK Fundamentals course`_ in the `Nordic Developer Academy`_ describes how to add sensors in Lesson 6.
* `nRF Connect SDK Intermediate course`_ in the `Nordic Developer Academy`_ describes how to add drivers in Lesson 7.

[source](https://academy.nordicsemi.com/courses/nrf-connect-sdk-intermediate/lessons/lesson-7-device-driver-model/topic/exercise-1-13/#Exercise-steps)


[source](https://academy.nordicsemi.com/courses/nrf-connect-sdk-intermediate/lessons/lesson-7-device-driver-model/topic/exercise-1-13/#Exercise-steps)

4. **Add the driver to the device tree**: Drivers are specified through the `compatible` property in the Device Tree. You need to add your driver to the device tree of your board [source](https://academy.nordicsemi.com/courses/nrf-connect-sdk-intermediate/lessons/lesson-3-adding-custom-board-support/topic/board-definition/).

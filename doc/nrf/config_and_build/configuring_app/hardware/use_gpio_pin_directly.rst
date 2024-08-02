.. _config_gpio_pin:

Driving a GPIO pin directly
###########################

.. contents::
   :local:
   :depth: 2

This user guide shows how to define, configure, and implement a GPIO pin directly using a binding for Nordic Semiconductor devices.
In the development phase of an embedded project, you can use this configuration to collect execution timings, or as a debugging tool.

You can apply this configuration manually in the devicetree overlay files or using the `Devicetree Visual Editor <How to work with Devicetree Visual Editor_>`_ (either in GUI or text mode) in the |nRFVSC|.

.. rst-class:: numbered-step

Define the DTS binding
**********************

You need to define the new GPIO pin node for the pin to be recognized by DTS.

If you work with a Nordic Semiconductor device, you can use the binding definition in :file:`dts/bindings/gpio`.

See Zephyr's documentation about :ref:`dt-bindings` for more information.

.. rst-class:: numbered-step

Configure the GPIO pin through DTS
**********************************

To declare a GPIO pin node, create a DTS node in the DTS of your board, application, or overlay file.
Pins defined this way can be accessed using devicetree macros.

If your application does not use the same GPIO instance as used by the node, enable the GPIO port instance required by the GPIO driver.

The following snippet shows the declaration of a GPIO pin node:

.. code-block:: c

	/ {
		user_dbg_pin: user-dbg-pin {
			compatible = "nordic,gpio-pins";
			gpios = <&gpio0 2 GPIO_ACTIVE_HIGH>;
			status = "okay";
		};
	};

	&gpio0 {
		status = "okay";
	};

	&gpiote0 {
		status = "okay";
	};

In this snippet:

* The node is labelled as ``user-dbg-pin``.
* ``compatible`` specifies the binding definition to be used (``nordic,gpio-pins`` from :file:`dts/bindings/gpio`).
* ``gpios`` specifies which pin node is being used (**Pin 2** of **GPIO0**).
* ``status`` enables the pin node when it is set to ``"okay"``.
* Additionally, the ``gpio0`` instance and ``gpiote0`` are enabled, so the GPIO driver can be built and executed.

.. rst-class:: numbered-step

Include the pin in your application
***********************************

To let your application access the declared pins, use the following devicetree macros:

1. Declare a GPIO struct instance in your application to allow the GPIO driver API to access the pin:

   .. code-block:: c

       #include <zephyr/drivers/gpio.h>
       static const struct gpio_dt_spec pin_dbg =
          GPIO_DT_SPEC_GET_OR(DT_NODELABEL(user_dbg_pin), gpios, {0});

#. Make sure your application initializes the pin:

   .. code-block:: c

       if (pin_dbg.port) {
          gpio_pin_configure_dt(&pin_dbg, GPIO_OUTPUT_INACTIVE);
    }

#. Add the following code where needed to let your application drive the pin:

   .. code-block:: c

      if (pin_dbg.port) {
         gpio_pin_set_dt(&pin_dbg, 1);
      }
      ...
      if (pin_dbg.port) {
         gpio_pin_set_dt(&pin_dbg, 0);
      }

The snippets above show an easy way of generating a square wave that reflects your software execution timings and state.
Such a plot can be observed using a logic analyzer or an oscilloscope.
Additionally, the code rendered through the snippets is dependent on the binding existence ``if (pin_dbg.port)``.
This means the snippets will be inactive when you build your application without declaring ``user-dbg-pin``.
This is an easy way to disable this debugging infrastructure.

Declaring multiple pins
***********************

You can also declare multiple pins in one GPIO property.
See the following code snippet:

.. code-block:: c

	/ {
		user_dbg_pin: user-dbg-pin {
			compatible = "nordic,gpio-pins";
			gpios = <&gpio0 2 GPIO_ACTIVE_HIGH>, <&gpio0 3 GPIO_ACTIVE_HIGH>;
			gpio-names = "enter", "exit";
			status = "okay";
		};
	};

To initialize the defined GPIO pin structures, use the ``GPIO_DT_SPEC_INST_GET_BY_IDX_OR()`` macro:

.. code-block:: c

   #include <zephyr/drivers/gpio.h>
   static const struct gpio_dt_spec pin_dbg0 =
       GPIO_DT_SPEC_GET_BY_IDX_OR(DT_NODELABEL(user_dbg_pin), gpios, 0, {0});
   static const struct gpio_dt_spec pin_dbg1 =
	   GPIO_DT_SPEC_GET_BY_IDX_OR(DT_NODELABEL(user_dbg_pin), gpios, 1, {0});

The rest of the GPIO pin operations follow the same process in case of declaring a single pin.

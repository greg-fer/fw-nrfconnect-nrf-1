.. _nrfx_usage:

Using nrfx drivers for nRF SoC peripherals
##########################################

.. contents::
   :local:
   :depth: 2

Introduction
************

nrfx is Nordic Semiconductor's hardware abstraction layer (HAL) library that provides low-level drivers for nRF SoC peripherals.
In the |NCS|, nrfx serves as the foundation layer between Zephyr's device model and the Nordic hardware.

The |NCS| integrates nrfx through the ``hal_nordic`` module, making nrfx drivers available for direct use in your applications.
While Zephyr drivers typically wrap nrfx APIs to provide a standardized interface, you can also use nrfx drivers directly when you need:

* Hardware-level control and optimization
* Access to peripheral features not exposed through Zephyr drivers
* Direct hardware event-to-task connections using GPPI/PPI
* Low-latency operations that bypass the Zephyr device model

For more information about nrfx, see the `nrfx repository`_ and the `nrfx API documentation`_.

.. note::
   The nrfx library is automatically included in the |NCS| build system for Nordic Semiconductor SoCs.
   You do not need to manually add it as a dependency.

Quick start
***********

Basic workflow for using nrfx drivers:

1. Enable the driver in :file:`prj.conf` (for example, ``CONFIG_NRFX_GPIOTE=y``).
2. Include the driver header (for example, ``#include <nrfx_gpiote.h>``).
3. Get the driver instance (devicetree or direct).
4. Initialize and configure the peripheral.
5. Set up interrupts if needed.

Enabling nrfx drivers
*********************

nrfx drivers are enabled through Kconfig options.
The :kconfig:option:`CONFIG_HAS_NRFX` option is automatically enabled for Nordic Semiconductor SoCs.

To enable a specific nrfx driver, add the corresponding Kconfig option to your :file:`prj.conf`:

.. code-block:: kconfig

   CONFIG_NRFX_GPIOTE=y
   CONFIG_NRFX_TIMER=y
   CONFIG_NRFX_GPPI=y

Common driver options:

* :kconfig:option:`CONFIG_NRFX_GPIOTE` - GPIOTE driver
* :kconfig:option:`CONFIG_NRFX_TIMER` - Timer driver
* :kconfig:option:`CONFIG_NRFX_GPPI` - GPPI driver
* :kconfig:option:`CONFIG_NRFX_SPIM0`, :kconfig:option:`CONFIG_NRFX_SPIM1`, etc. - SPI Master drivers
* :kconfig:option:`CONFIG_NRFX_TWIM0`, :kconfig:option:`CONFIG_NRFX_TWIM1`, etc. - I2C Master drivers
* :kconfig:option:`CONFIG_NRFX_SAADC` - ADC driver
* :kconfig:option:`CONFIG_NRFX_PWM` - PWM driver

For a complete list, see Kconfig files in the nrfx module or :file:`tests/drivers/nrfx_integration_test/Kconfig`.

Including headers
*****************

Include driver headers following the pattern :file:`nrfx_<peripheral>.h`:

.. code-block:: c

   #include <nrfx_gpiote.h>
   #include <nrfx_timer.h>
   #include <helpers/nrfx_gppi.h>

For devicetree integration helpers:

.. code-block:: c

   #include <gpiote_nrfx.h>

For direct hardware register access:

.. code-block:: c

   #include <hal/nrf_gpiote.h>
   #include <hal/nrf_timer.h>

Getting driver instances
************************



Devicetree integration (recommended)
=====================================

Use devicetree helpers to get instances from GPIO pin nodes:

.. code-block:: c

   #include <gpiote_nrfx.h>
   #include <zephyr/devicetree.h>

   #define GPIOTE_NODE NRF_DT_GPIOTE_NODE(DT_ALIAS(led0), gpios)
   nrfx_gpiote_t *gpiote = &GPIOTE_NRFX_INST_BY_NODE(GPIOTE_NODE);

GPIOTE instances obtained via devicetree are pre-initialized.
For other peripherals, check if initialization is required using ``nrfx_<peripheral>_init_check()``.

Direct instance macros
======================

For peripherals without devicetree helpers or when using specific instances:

.. code-block:: c

   static nrfx_timer_t timer = NRFX_TIMER_INSTANCE(NRF_TIMER1);
   static nrfx_spim_t spim = NRFX_SPIM_INSTANCE(NRF_SPIM0);

Initialization and setup
************************

GPIOTE
======

GPIOTE instances from devicetree are pre-initialized.
For direct instances, initialize first:

.. code-block:: c

   if (!nrfx_gpiote_init_check(gpiote)) {
       nrfx_gpiote_init(gpiote, 0);
   }

Configure output pin with task:

.. code-block:: c

   uint8_t ch;
   nrfx_gpiote_channel_alloc(gpiote, &ch);
   const nrfx_gpiote_output_config_t out_cfg = NRFX_GPIOTE_DEFAULT_OUTPUT_CONFIG;
   const nrfx_gpiote_task_config_t task_cfg = {
       .task_ch = ch,
       .polarity = NRF_GPIOTE_POLARITY_TOGGLE,
       .init_val = NRF_GPIOTE_INITIAL_VALUE_LOW,
   };
   nrfx_gpiote_output_configure(gpiote, PIN, &out_cfg, &task_cfg);
   nrfx_gpiote_out_task_enable(gpiote, PIN);

Configure input pin with trigger:

.. code-block:: c

   uint8_t ch;
   nrfx_gpiote_channel_alloc(gpiote, &ch);
   nrfx_gpiote_trigger_config_t trig_cfg = {
       .p_in_channel = &ch,
       .trigger = NRFX_GPIOTE_TRIGGER_LOTOHI,
   };
   nrf_gpio_pin_pull_t pull = NRFX_GPIOTE_DEFAULT_PULL_CONFIG;
   nrfx_gpiote_input_pin_config_t in_cfg = {
       .p_pull_config = &pull,
       .p_trigger_config = &trig_cfg,
   };
   nrfx_gpiote_input_configure(gpiote, PIN, &in_cfg);
   nrfx_gpiote_trigger_enable(gpiote, PIN, false);

Timer
=====

Initialize timer:

.. code-block:: c

   static nrfx_timer_t timer = NRFX_TIMER_INSTANCE(NRF_TIMER1);
   nrfx_timer_config_t cfg = NRFX_TIMER_DEFAULT_CONFIG(
       NRFX_TIMER_BASE_FREQUENCY_GET(&timer));
   cfg.bit_width = NRF_TIMER_BIT_WIDTH_32;
   cfg.mode = NRF_TIMER_MODE_TIMER;
   nrfx_timer_init(&timer, &cfg, timer_handler);
   nrfx_timer_enable(&timer);

For timer interrupts, connect IRQ handler:

.. code-block:: c

   IRQ_CONNECT(DT_IRQN(DT_NODELABEL(timer1)),
               DT_IRQ(DT_NODELABEL(timer1), priority),
               nrfx_timer_irq_handler,
               &timer,
               0);
   irq_enable(DT_IRQN(DT_NODELABEL(timer1)));

GPPI/PPI connection
=================

Connect events to tasks in hardware:

.. code-block:: c

   uint32_t evt = nrfx_gpiote_in_event_address_get(gpiote, PIN);
   uint32_t task = nrfx_timer_task_address_get(&timer, NRF_TIMER_TASK_COUNT);
   nrfx_gppi_handle_t handle;
   nrfx_gppi_conn_alloc(evt, task, &handle);
   nrfx_gppi_conn_enable(handle);

IRQ handler setup
=================

Regular interrupt handler:

.. code-block:: c

   void handler(const struct device *dev, void *user_data)
   {
       nrfx_gpiote_irq_handler();
   }
   IRQ_CONNECT(DT_IRQN(DT_NODELABEL(gpiote)),
               DT_IRQ(DT_NODELABEL(gpiote), priority),
               handler, NULL, 0);
   irq_enable(DT_IRQN(DT_NODELABEL(gpiote)));

Direct interrupt handler (zero-latency):

.. code-block:: c

   ISR_DIRECT_DECLARE(isr_wrapper)
   {
       nrfx_gpiote_irq_handler();
       ISR_DIRECT_PM();
       return 1;
   }
   IRQ_DIRECT_CONNECT(DT_IRQN(DT_NODELABEL(gpiote)),
                      DT_IRQ(DT_NODELABEL(gpiote), priority),
                      isr_wrapper,
                      DT_IRQ(DT_NODELABEL(gpiote), flags));

Error handling
***************

nrfx functions return ``nrfx_err_t`` values:

* ``NRFX_SUCCESS`` - Operation successful
* ``NRFX_ERROR_INVALID_PARAM`` - Invalid parameter
* ``NRFX_ERROR_NO_MEM`` - Insufficient memory (e.g., no available channels)
* ``NRFX_ERROR_INVALID_STATE`` - Invalid state for operation
* ``NRFX_ERROR_NOT_SUPPORTED`` - Feature not supported

GPPI functions return negative values on error (typically ``-ENOMEM`` for channel exhaustion).

Always check return values and handle errors appropriately:

.. code-block:: c

   uint8_t ch;
   if (nrfx_gpiote_channel_alloc(gpiote, &ch) != NRFX_SUCCESS) {
       /* Handle channel exhaustion */
       return -ENOMEM;
   }

Resource cleanup
****************

Free allocated resources when no longer needed:

.. code-block:: c

   nrfx_gpiote_channel_free(gpiote, channel);
   nrfx_gppi_conn_free(gppi_handle);
   nrfx_timer_uninit(&timer);

Memory section requirements
****************************

EasyDMA peripherals (SPI, UART, etc.) require buffers in specific memory sections:

.. code-block:: c

   #include <zephyr/linker/devicetree_regions.h>

   #define MEMORY_SECTION(node) \
       COND_CODE_1(DT_NODE_HAS_PROP(node, memory_regions), \
           (__attribute__((__section__( \
               LINKER_DT_NODE_REGION_NAME(DT_PHANDLE(node, memory_regions)))))), \
           ())

   static uint8_t buffer[256] MEMORY_SECTION(DT_NODELABEL(spi0));

Example: Button and LED with GPPI
*********************************

Hardware connection of button event to LED toggle task:

.. code-block:: kconfig

   CONFIG_NRFX_GPIOTE=y
   CONFIG_NRFX_GPPI=y
   CONFIG_GPIO=n

.. code-block:: c

   #include <zephyr/kernel.h>
   #include <zephyr/devicetree.h>
   #include <nrfx_gpiote.h>
   #include <gpiote_nrfx.h>
   #include <helpers/nrfx_gppi.h>
   #include <zephyr/irq.h>

   #define BUTTON_NODE DT_ALIAS(sw0)
   #define LED_NODE DT_ALIAS(led0)
   #define BUTTON_GPIOTE_NODE NRF_DT_GPIOTE_NODE(BUTTON_NODE, gpios)
   #define LED_GPIOTE_NODE NRF_DT_GPIOTE_NODE(LED_NODE, gpios)
   #define BUTTON_PIN NRF_DT_GPIOS_TO_PSEL(BUTTON_NODE, gpios)
   #define LED_PIN NRF_DT_GPIOS_TO_PSEL(LED_NODE, gpios)

   static nrfx_gpiote_t *button_gpiote = &GPIOTE_NRFX_INST_BY_NODE(BUTTON_GPIOTE_NODE);
   static nrfx_gpiote_t *led_gpiote = &GPIOTE_NRFX_INST_BY_NODE(LED_GPIOTE_NODE);
   static nrfx_gppi_handle_t gppi_handle;

   ISR_DIRECT_DECLARE(gpiote_isr)
   {
       nrfx_gpiote_irq_handler();
       ISR_DIRECT_PM();
       return 1;
   }

   int main(void)
   {
       uint8_t btn_ch, led_ch;

       nrfx_gpiote_channel_alloc(button_gpiote, &btn_ch);
       nrfx_gpiote_trigger_config_t trig = {
           .p_in_channel = &btn_ch,
           .trigger = NRFX_GPIOTE_TRIGGER_LOTOHI,
       };
       nrf_gpio_pin_pull_t pull = NRF_GPIO_PIN_PULLUP;
       nrfx_gpiote_input_pin_config_t in_cfg = {
           .p_pull_config = &pull,
           .p_trigger_config = &trig,
       };
       nrfx_gpiote_input_configure(button_gpiote, BUTTON_PIN, &in_cfg);
       nrfx_gpiote_trigger_enable(button_gpiote, BUTTON_PIN, false);

       nrfx_gpiote_channel_alloc(led_gpiote, &led_ch);
       const nrfx_gpiote_output_config_t out_cfg = NRFX_GPIOTE_DEFAULT_OUTPUT_CONFIG;
       const nrfx_gpiote_task_config_t task_cfg = {
           .task_ch = led_ch,
           .polarity = NRF_GPIOTE_POLARITY_TOGGLE,
           .init_val = NRF_GPIOTE_INITIAL_VALUE_LOW,
       };
       nrfx_gpiote_output_configure(led_gpiote, LED_PIN, &out_cfg, &task_cfg);
       nrfx_gpiote_out_task_enable(led_gpiote, LED_PIN);

       uint32_t evt = nrfx_gpiote_in_event_address_get(button_gpiote, BUTTON_PIN);
       uint32_t task = nrfx_gpiote_out_task_address_get(led_gpiote, LED_PIN);
       nrfx_gppi_conn_alloc(evt, task, &gppi_handle);
       nrfx_gppi_conn_enable(gppi_handle);

       IRQ_DIRECT_CONNECT(DT_IRQN(DT_NODELABEL(gpiote)),
                          DT_IRQ(DT_NODELABEL(gpiote), priority),
                          gpiote_isr,
                          DT_IRQ(DT_NODELABEL(gpiote), flags));
       irq_enable(DT_IRQN(DT_NODELABEL(gpiote)));

       while (1) {
           k_sleep(K_SECONDS(1));
       }
   }

Integration considerations
**************************

When to use nrfx directly vs Zephyr drivers
============================================

Use nrfx directly when:

* You need hardware-level features not exposed through Zephyr drivers
* You want to connect peripheral events to tasks using GPPI/PPI
* You require low-latency operations that bypass the Zephyr device model
* You need precise timing control for time-critical operations
* You're implementing custom drivers or middleware

Use Zephyr drivers when:

* You want portable code that works across different SoC vendors
* You need standard APIs that integrate with Zephyr subsystems
* You're building general-purpose applications
* You want automatic resource management through the device model

Resource sharing
================

* Multiple drivers (Zephyr and nrfx) should not access the same peripheral instance simultaneously
* GPIOTE channels are shared resources - allocate carefully and free when done
* GPPI/PPI channels are limited - check availability before allocation
* Some peripherals may be used by Zephyr drivers - check devicetree configuration

Common pitfalls
===============

* **GPIOTE channel exhaustion**: Check return values from ``nrfx_gpiote_channel_alloc()`` and free unused channels
* **GPPI channel limits**: GPPI channels are limited per SoC - handle allocation failures gracefully
* **Driver conflicts**: Disable conflicting Zephyr drivers (e.g., ``CONFIG_GPIO=n`` when using nrfx GPIOTE directly)
* **Missing IRQ setup**: Timer and other interrupt-driven peripherals require IRQ connection
* **Memory section requirements**: EasyDMA peripherals require buffers in specific memory sections
* **Interrupt priority**: Ensure interrupt priorities are appropriate for your use case

Additional resources
********************

* `nrfx API documentation`_ - Complete API reference for all nrfx drivers
* `nrfx repository`_ - Source code and issue tracking
* `Zephyr nrfx sample`_ - Example demonstrating nrfx usage in Zephyr
* :ref:`add_new_driver` - Guide for creating custom drivers
* :ref:`use_gpio_pin_directly` - Alternative approach using Zephyr GPIO APIs

Related NCS samples
===================

The following NCS samples demonstrate nrfx usage:

* :file:`samples/bluetooth/iso_time_sync` - Uses nrfx GPIOTE and GPPI for timed LED control
* :file:`tests/drivers/spi/spim_mosi_toggles` - Demonstrates nrfx GPIOTE, Timer, and GPPI integration

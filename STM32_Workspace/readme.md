# STM32 Bare-Metal Embedded Systems Projects

## Overview
This repository contains a collection of embedded C projects developed for the STM32 microcontroller family. All projects in this repository are written from scratch using a **Bare-Metal** approach. No Hardware Abstraction Layer (HAL) or standard peripheral libraries were used. Every peripheral is controlled via direct memory-mapped register manipulation, demonstrating a deep understanding of the ARM Cortex-M architecture and microcontroller internals.

These projects were developed in conjunction with the highly acclaimed **"Advanced Embedded Systems Bare-Metal Programming Ground Up™"** course by Israel Gbati on Udemy.

## Key Concepts & Features Implemented
By interacting directly with the MCU registers, these projects cover the fundamental building blocks of embedded systems:

*   **Clock Configuration:** Direct manipulation of the RCC (Reset and Clock Control) registers to configure system clocks and peripheral buses.
*   **GPIO Interface:** Bare-metal initialization and control of General-Purpose Input/Output pins.
*   **UART/USART Communication:** Developing custom serial communication drivers for debugging and data transmission.
*   **Timers & Delays:** Configuring hardware timers (SysTick and General Purpose Timers) for precise timekeeping and PWM generation.
*   **Interrupts (NVIC):** Handling hardware interrupts and configuring the Nested Vectored Interrupt Controller.
*   **Analog-to-Digital Conversion (ADC):** Configuring the ADC peripheral for reading analog sensor data.
*   **I2C & SPI Protocols:** Bare-metal implementation of synchronous serial communication protocols.

## Hardware & Tools
*   **Microcontroller:** STM32F411RE Nucleo-64
*   **Architecture:** ARM Cortex-M
*   **Language:** Embedded C
*   **IDE / Toolchain:** STM32CubeIDE

##  Why Bare-Metal?
While HAL libraries speed up development time, writing code at the register level ensures:
1.  **Optimized Performance:** Lower execution overhead compared to heavily abstracted libraries.
2.  **Memory Efficiency:** Significantly reduced code footprint (Flash/RAM usage).
3.  **Deep Hardware Knowledge:** Total control over the hardware behavior and a thorough understanding of the MCU's reference manual and datasheet.

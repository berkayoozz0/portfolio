### AC/DC Powered ATmega328P Control Board

A versatile, dual-powered control board built around the robust ATmega328P microcontroller. This system is engineered for maximum flexibility, capable of safely interfacing with 220V AC mains while providing seamless plug-and-play programming and peripheral control.

*   **Power Management & Selection:** Designed to be powered by either a directly connected 220V AC mains input (utilizing onboard AC-DC and DC-DC conversion stages) or a 5V USB Type-C connection. It features an integrated power select circuit for seamless and safe switching between power sources.
*   **Microcontroller:** At the heart of the board is the ATmega328P-PU, providing a reliable and robust processing unit for continuous industrial or automation tasks.
*   **Onboard Programming:** Integrated CH340C USB-to-Serial IC allows for seamless programming directly through the USB Type-C port, making it incredibly easy to interface with PCs and other devices without needing external FTDI adapters.
*   **Outputs & Connectivity:** 
    *   Dedicated 12V Fan output (featuring optocoupler isolation to protect the MCU).
    *   ADC output port for accurate analog sensor readings.
    *   UART communication interface.
    *   Comprehensive breakout headers providing easy, breadboard-friendly access to the microcontroller's GPIO pins.

<p align="center">
  <img src="image_e5a44f.png" alt="3D Render Front" width="800"/>
</p>

<p align="center">
  <img src="image_e5a432.jpg" alt="3D Render Back" width="800"/>
</p>

#### Hardware Schematics

**Microcontroller, Programming, and I/O Interfaces:**
![MCU and Interfaces Schematic](image_e5a42e.png)

**Power Supply & AC/DC Conversion Stage:**
![Power Stage Schematic](image_e5a473.jpg)
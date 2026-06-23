# CANbus to SPI Bridge Module

<img width="1600" height="1200" alt="3D_Top_View" src="[BURAYA_LINK_GELECEK]" />
<img width="1600" height="1200" alt="3D_Angle_View" src="[BURAYA_LINK_GELECEK]" />

## Project Overview
This repository contains the hardware design files for a custom CANbus-SPI Bridge module, completed as a 1-day design sprint. The primary function of this board is to act as a robust interface, enabling microcontrollers without native CAN capabilities to communicate seamlessly on industrial CAN networks by translating SPI data into standard differential CAN signals.

To achieve industrial-grade reliability and high signal integrity, the hardware architecture is designed with strict adherence to design rules:

### CAN Communication & Processing Core
A robust digital-to-analog interface designed to handle fast data conversion and provide a reliable physical layer for the CAN bus topology.
*  **CAN Controller:** MCP2515 (Stand-Alone CAN Controller with SPI Interface) for handling the CAN protocol overhead.
*  **CAN Transceiver:** TJA1050 (High-Speed CAN Transceiver) to drive the physical differential lines.
*  **Signal Integrity:** The `CAN_H` and `CAN_L` lines are meticulously routed as tightly coupled differential pairs. Stubs were eliminated to prevent signal reflection and ensure maximum noise immunity.
*  **Network Adaptability:** Integrated a selectable 120Ω termination resistor circuit with a jumper. Clearly labeled as `ON = END NODE` and `OFF = MID NODE` to easily adapt the module to any physical position within a CAN bus architecture.

### Power Management & Interface Stage
A clean power distribution and user-friendly interface stage to ensure stable operation and ease of use in the field.
*  **Power Distribution Network (PDN):** Applied strict through-pad routing techniques for the decoupling capacitors to provide clean power delivery to the ICs and minimize EMI.
*  **Connectivity & Interfaces:** Standard 2.54mm headers for SPI communication/power inputs, and rugged screw terminals for the CAN outputs.
*  **Industrial Silkscreen:** Field-wiring is made idiot-proof with clear labeling directly aligned with the screw terminals and pin headers.

<img width="1500" height="765" alt="Routing_View" src="[BURAYA_LINK_GELECEK]" />

## Key Features & Specifications
* **Layer Stackup:** 2-Layer PCB design featuring solid Ground (GND) polygon pours on both Top and Bottom layers to ensure a clean return path and reduce electromagnetic interference.
* **EDA Tool:** Designed completely from scratch using **Altium Designer**.

---
Designed by Berkay ÖZ
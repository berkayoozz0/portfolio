# CANbus to SPI Bridge Module

<img width="1543" height="1023" alt="3" src="https://github.com/user-attachments/assets/32f332ba-2650-4343-9251-855940fdf15a" />
<img width="1548" height="1023" alt="4" src="https://github.com/user-attachments/assets/285ca765-01fe-48d0-89af-0a7bc618265a" />
<img width="1548" height="1023" alt="5" src="https://github.com/user-attachments/assets/a9a8641b-d59c-4db4-88be-844f2bfa282d" />
<img width="1548" height="1023" alt="6" src="https://github.com/user-attachments/assets/4a5dbc4c-aa78-4a55-836d-ddb974c51c3e" />


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

<img width="1839" height="1068" alt="1" src="https://github.com/user-attachments/assets/3b01b73d-3c00-4408-b2ae-b42c3925fd95" />
<img width="1839" height="1065" alt="2" src="https://github.com/user-attachments/assets/f0698b3b-0035-47df-b31b-2265e3caad46" />

## Key Features & Specifications

<img width="1229" height="1050" alt="8" src="https://github.com/user-attachments/assets/64d81b45-4855-4765-9749-fb7cca28bf97" />
<img width="2486" height="694" alt="7" src="https://github.com/user-attachments/assets/7753b85e-aaa5-4712-8c82-3504337ca61a" />


* **Layer Stackup:** 2-Layer PCB design featuring solid Ground (GND) polygon pours on both Top and Bottom layers to ensure a clean return path and reduce electromagnetic interference.
* **EDA Tool:** Designed completely from scratch using **Altium Designer**.

---
Designed by Berkay ÖZ

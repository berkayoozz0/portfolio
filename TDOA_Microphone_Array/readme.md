# TDOA-Based Sound Source Localization System

<img width="1600" height="1200" alt="WhatsApp Image 2026-04-30 at 17 22 53" src="https://github.com/user-attachments/assets/c032fdfe-0046-4054-9924-cb4684bc398f" />
<img width="2325" height="1217" alt="Adsız" src="https://github.com/user-attachments/assets/8d16b9c6-5b33-4837-835f-9ca10c3303ba" />

<img width="2000" height="1500" alt="2" src="https://github.com/user-attachments/assets/0e9b66cd-ca58-421f-a0b8-786a072d9799" />
<img width="2325" height="1217" alt="ön" src="https://github.com/user-attachments/assets/46f9480d-f791-4b35-8732-bf4d43187ac0" />



## Project Overview
This repository contains the hardware designs for my senior graduation thesis project. The system is designed to detect and calculate the direction of a sound source in real-time using the **Time Difference of Arrival (TDOA)** algorithm. 

To achieve high accuracy and modularity, the hardware architecture is split into two custom-designed **4-layer PCBs**:
### Microphone & Analog Front-End Board
An acoustic front-end array designed to capture and amplify audio signals with minimal noise.
*  **Microphones:** Knowles FG-Series professional audio microphones.
*  **Preamplifier Stage:** OPA320 in a non-inverting configuration.
*  **Power Management:** Li-Polymer battery with Low-Noise LDO Regulator.
*  **Connectors:** 3.5mm audio jack
<img width="1549" height="1152" alt="Ekran görüntüsü 2026-04-30 174130" src="https://github.com/user-attachments/assets/3515ecdd-0be0-4ec2-bf5a-dcfd5f55191d" />



### Microcontroller & Signal Processing Board
A high-performance processing core designed to handle high-speed analog-to-digital conversion, robust signal conditioning, and complex TDOA algorithm execution.
*  **Microcontroller:** STM32H743VIT6 (ARM Cortex-M7) operating with a 25MHz external crystal and comprehensive decoupling/bypassing networks.
*  **Signal Conditioning Stage:** Pseudo-differential inputs utilizing AD8276 difference amplifiers to maximize common-mode noise rejection before ADC sampling.
*  **Power Management:** Regulated 3.3V supply via AMS1117 LDO, equipped with EMI filtering and strategic test points for hardware bring-up.
*  **Connectivity & Interfaces:** USB Type-C with USBLC6 ESD protection and Common-Mode Choke (90R), 3.5mm audio inputs (PESD3V3L1BA protected), SWD debugging port, and UART output.
<img width="1120" height="1159" alt="Ekran görüntüsü 2026-04-30 174710" src="https://github.com/user-attachments/assets/40ebe2af-9075-4fc6-b1aa-48cc6abbf04d" />

## Key Features & Specifications
* **Layer Stackup:** 4-Layer PCB design (Power+Signal - Ground - Ground - Power+Signal) with proper impedance control and ground shielding to ensure signal integrity for mixed-signal routing.
* **EDA Tool:** Designed completely from scratch using **KiCad**.


---
*Designed by Berkay ÖZ

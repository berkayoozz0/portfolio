# TDOA-Based Sound Source Localization System

<img width="1600" height="1200" alt="WhatsApp Image 2026-04-30 at 17 22 53" src="https://github.com/user-attachments/assets/c032fdfe-0046-4054-9924-cb4684bc398f" />
<img width="2000" height="1500" alt="2" src="https://github.com/user-attachments/assets/0e9b66cd-ca58-421f-a0b8-786a072d9799" />


<img width="2325" height="1217" alt="Adsız" src="https://github.com/user-attachments/assets/8d16b9c6-5b33-4837-835f-9ca10c3303ba" />
<img width="2325" height="1217" alt="ön" src="https://github.com/user-attachments/assets/46f9480d-f791-4b35-8732-bf4d43187ac0" />



## Project Overview
This repository contains the hardware designs for my senior graduation thesis project. The system is designed to detect and calculate the direction of a sound source in real-time using the **Time Difference of Arrival (TDOA)** algorithm. 

To achieve high accuracy and modularity, the hardware architecture is split into two custom-designed **4-layer PCBs**:
1. **Microphone Board:** An acoustic front-end array designed to capture and amplify audio signals with minimal noise.
2. **Microcontroller Board:** The processing unit responsible for sampling the audio data, executing the TDOA mathematical model, and determining the localization vector.

## Key Features & Specifications
* **Hardware Stack:** 4-Layer PCB design with proper impedance control and ground shielding to ensure signal integrity for mixed-signal routing.
* **EDA Tool:** Designed completely from scratch using **KiCad**.

# TDOA-Based Sound Source Localization System


## Project Overview
This repository contains the hardware designs for my senior graduation thesis project. The system is designed to detect and calculate the direction of a sound source in real-time using the **Time Difference of Arrival (TDOA)** algorithm. 

To achieve high accuracy and modularity, the hardware architecture is split into two custom-designed **4-layer PCBs**:
1. **Microphone Board:** An acoustic front-end array designed to capture and amplify audio signals with minimal noise.
2. **Microcontroller Board:** The processing unit responsible for sampling the audio data, executing the TDOA mathematical model, and determining the localization vector.

## Key Features & Specifications
* **Hardware Stack:** 4-Layer PCB design with proper impedance control and ground shielding to ensure signal integrity for mixed-signal routing.
* **EDA Tool:** Designed completely from scratch using **KiCad**.

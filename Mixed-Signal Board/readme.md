# Mixed-Signal Data Acquisition & Processing Board

<p align="center">
  <img width="2290" height="1200" alt="önkart1" src="https://github.com/user-attachments/assets/58ca45e1-5166-4cc5-a53e-bd30823a0357" />
</p>
<p align="center">
<img width="2282" height="1198" alt="yan" src="https://github.com/user-attachments/assets/aedbcbda-7952-4215-95fb-e66b2fb5df17" />
</p>
<p align="center">
  <img width="2287" height="1202" alt="arkakart" src="https://github.com/user-attachments/assets/15617b81-86e8-4098-9871-f5b921eef474" />
</p>

## Project Overview
This repository contains a high-performance mixed-signal hardware design, developed as part of the **"Mixed-Signal Hardware Design with KiCad"** course by Philip Salmony (Phil's Lab) on FEDEVEL Academy. 

The board is engineered to perform precision analog-to-digital (ADC) and digital-to-analog (DAC) conversions while maintaining strict isolation between noisy digital circuits and sensitive analog front-ends. It is capable of processing audio-band frequencies ($20\text{Hz} < \text{BW} < 20\text{kHz}$) with robust anti-aliasing and reconstruction filters.

## Hardware Architecture & Key Stages

### Analog Input Stage (ADC)
Designed to safely capture external signals and prepare them for high-resolution sampling.
*   **Input:** BNC connector with robust ESD protection (PESD3V3L1BA) and a 1.4Hz High-Pass filter to remove DC offset.
*   **Signal Conditioning:** Unity-gain buffered by an MCP6001 op-amp, followed by a **3rd-order Butterworth Anti-Aliasing Low-Pass Filter** ($f_c = 25\text{ kHz}$) to prevent out-of-band noise folding.
*   **Conversion:** Single-ended to balanced conversion feeding into a **14-bit ADC** (ADC141S626) via SPI.
*   **Operating Range:** Accurately processes input voltages from $-1.65\text{V}$ to $+1.65\text{V}$.
  <img width="1804" height="1022" alt="Ekran görüntüsü 2026-04-30 181551" src="https://github.com/user-attachments/assets/8271623c-7735-4ba2-a9d5-1cc1f214e739" />

### Analog Output Stage (DAC)
Engineered for clean, low-noise signal generation.
*   **Generation:** 16-bit DAC (DAC7563) driven via SPI.
*   **Reconstruction:** The DAC output is passed through a **3rd-order Butterworth Reconstruction Low-Pass Filter** ($f_c = 25\text{ kHz}$) utilizing MCP6001 op-amps to smooth the quantized steps.
*   **Output:** BNC connector with a $50\Omega$ output impedance and a voltage range of $0\text{V}$ to $+3.3\text{V}$.
 <p align="center">
    <img width="1759" height="536" alt="Ekran görüntüsü 2026-04-30 181557" src="https://github.com/user-attachments/assets/3ba67067-8f45-476b-9c51-58f40c08d70c" />
 </p>
 
### Microcontroller Core
*   **MCU:** STM32F103CBT6 (ARM Cortex-M3) running at 16MHz (external crystal).
*   **Connectivity:** Modern USB Type-C interface, heavily protected with USBLC6-2SC6 ESD diodes and a $90\Omega$ Common-Mode Choke for EMI suppression.
*   **Debugging:** Standard SWD interface.
  <p align="center">
    <img width="1802" height="1142" alt="Ekran görüntüsü 2026-04-30 181543" src="https://github.com/user-attachments/assets/4717d0cc-d403-4611-ae4c-eeb58eb414d9" />
  </p>
   
### Power Management
To ensure the digital switching noise does not couple into the analog measurements, the power delivery is strictly divided:
*   **Digital Power (+3V3):** Stepped down from USB 5V VBUS using a TLV62569 Buck Converter for high efficiency.
*   **Analog Power (+3.3VA):** Derived from a dedicated LC-filtered 5V rail and regulated by a low-noise HT7533-1 LDO to provide a pristine supply for op-amps and data converters.
*   **Reference Voltage:** A dedicated REF3033 precision reference generator supplies an ultra-stable $3.3\text{V}$ to the ADC.
  <img width="1781" height="939" alt="Ekran görüntüsü 2026-04-30 181526" src="https://github.com/user-attachments/assets/94c6fee1-04be-4ffb-bee3-07c0229ae084" />

### PCB Layout (Mixed-Signal Grounding)
Notice the careful component placement and routing to separate the digital return currents from the sensitive analog return paths.
<img width="899" height="1099" alt="Ekran görüntüsü 2026-04-30 181707" src="https://github.com/user-attachments/assets/9280366a-11b7-47e5-af74-ffca73180e5a" />






---
*Designed with KiCad*

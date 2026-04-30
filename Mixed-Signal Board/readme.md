# Mixed-Signal Data Acquisition & Processing Board

<p align="center">
  <img src="image_e5a44f.png" alt="3D Render Front" width="800"/>
</p>
<p align="center">
  <img src="image_e5a432.jpg" alt="3D Render Back" width="800"/>
</p>

## 📌 Project Overview
This repository contains a high-performance mixed-signal hardware design, developed as part of the **"Mixed-Signal Hardware Design with KiCad"** course by Philip Salmony (Phil's Lab) on FEDEVEL Academy. 

The board is engineered to perform precision analog-to-digital (ADC) and digital-to-analog (DAC) conversions while maintaining strict isolation between noisy digital circuits and sensitive analog front-ends. It is capable of processing audio-band frequencies ($20\text{Hz} < \text{BW} < 20\text{kHz}$) with robust anti-aliasing and reconstruction filters.

## 🛠️ Hardware Architecture & Key Stages

### 1. Analog Input Stage (ADC)
Designed to safely capture external signals and prepare them for high-resolution sampling.
*   **Input:** BNC connector with robust ESD protection (PESD3V3L1BA) and a 1.4Hz High-Pass filter to remove DC offset.
*   **Signal Conditioning:** Unity-gain buffered by an MCP6001 op-amp, followed by a **3rd-order Butterworth Anti-Aliasing Low-Pass Filter** ($f_c = 25\text{ kHz}$) to prevent out-of-band noise folding.
*   **Conversion:** Single-ended to balanced conversion feeding into a **14-bit ADC** (ADC141S626) via SPI.
*   **Operating Range:** Accurately processes input voltages from $-1.65\text{V}$ to $+1.65\text{V}$.

### 2. Analog Output Stage (DAC)
Engineered for clean, low-noise signal generation.
*   **Generation:** 16-bit DAC (DAC7563) driven via SPI.
*   **Reconstruction:** The DAC output is passed through a **3rd-order Butterworth Reconstruction Low-Pass Filter** ($f_c = 25\text{ kHz}$) utilizing MCP6001 op-amps to smooth the quantized steps.
*   **Output:** BNC connector with a $50\Omega$ output impedance and a voltage range of $0\text{V}$ to $+3.3\text{V}$.

### 3. Microcontroller Core
*   **MCU:** STM32F103CBT6 (ARM Cortex-M3) running at 16MHz (external crystal).
*   **Connectivity:** Modern USB Type-C interface, heavily protected with USBLC6-2SC6 ESD diodes and a $90\Omega$ Common-Mode Choke for EMI suppression.
*   **Debugging:** Standard SWD interface.

### 4. Power Management (Split-Rail Topology)
To ensure the digital switching noise does not couple into the analog measurements, the power delivery is strictly divided:
*   **Digital Power (+3V3):** Stepped down from USB 5V VBUS using a TLV62569 Buck Converter for high efficiency.
*   **Analog Power (+3.3VA):** Derived from a dedicated LC-filtered 5V rail and regulated by a low-noise HT7533-1 LDO to provide a pristine supply for op-amps and data converters.
*   **Reference Voltage:** A dedicated REF3033 precision reference generator supplies an ultra-stable $3.3\text{V}$ to the ADC.

## 📸 Schematics & Layout

### PCB Layout (Mixed-Signal Grounding)
Notice the careful component placement and routing to separate the digital return currents from the sensitive analog return paths.
![PCB Layout](Ekran görüntüsü 2026-04-30 180225.jpg)

### Analog Front-End (Input & Output)
![Analog Stage Schematic](Ekran görüntüsü 2026-04-30 180556.png)

### ADC & DAC Subsystems
![Data Converters Schematic](Ekran görüntüsü 2026-04-30 180626.png)

---
*Designed with KiCad*
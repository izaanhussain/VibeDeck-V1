# VibeDeck-V1
A custom 3×3 macropad built from scratch with a XIAO RP2040, custom PCB, and 3D-printed case. I made this for hackclub embassy

<img width="977" height="743" alt="WhatsApp Image 2026-11-08 at 1 47 49 PM" src="https://github.com/user-attachments/assets/d52fdcd4-e877-464e-91b4-8aa1071fd62a" />


## Features

* 9 programmable keys
* EC11 rotary encoder with push button
* 0.91" OLED display
* Custom PCB designed in KiCad
* 3D-printed two-piece case
* QMK firmware
* DSA keycaps
 

# PCB 
The PCB is made in Kicad

<img width="631" height="699" alt="image" src="https://github.com/user-attachments/assets/1b2e9a4e-2680-4fb9-8c8a-fdd011eb03df" />

<img width="802" height="624" alt="image" src="https://github.com/user-attachments/assets/c2662e9d-ed01-4e3d-af60-9538d57e4167" />

# Schematic

<img width="845" height="591" alt="image" src="https://github.com/user-attachments/assets/5cb51dbd-4600-4ca7-bab1-a474490a98a0" />

# Case

<img width="977" height="743" alt="WhatsApp Image 2026-11-08 at 1 47 49 PM" src="https://github.com/user-attachments/assets/71077600-af35-4e7f-afd6-d5293a5dc749" />


## BOM

| Quantity | Part                               |
| -------- | ---------------------------------- |
| 1        | XIAO RP2040                        |
| 9        | 1N4148 Diodes                      |
| 9        | Cherry MX Switches                 |
| 1        | EC11E Rotary Encoder (with switch) |
| 1        | 0.91" OLED Display                 |
| 9        | DSA Keycaps                        |
| 4        | M3×16mm Screws                     |
| 4        | M3×5mm×4mm Heatset Inserts         |
| 1        | 3D-Printed Case (Top + Bottom)     |

## Firmware
VibeDeck uses KMK firmware with CircuitPython, located in the Firmware directory

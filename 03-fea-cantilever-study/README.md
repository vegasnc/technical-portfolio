# Cantilever Beam Analysis

This project provides an analytical benchmark for a rectangular beam fixed at one end and loaded at the other.

## Model

| Parameter | Value |
|---|---:|
| Length | 150 mm |
| Width | 20 mm |
| Thickness | 6 mm |
| End load | 100 N |
| Young's modulus | 200 GPa |

## Calculated results

- Second moment of area: 3.60 × 10⁻⁹ m⁴
- Nominal bending stress: approximately 125 MPa
- Tip deflection: approximately 0.781 mm

The results come from elementary beam theory. They are not outputs from COMSOL or another finite element solver. The model assumes linear-elastic behavior and small deflection, and does not assess fatigue, buckling, or safety factors.

Run `beam_calculation.py` to reproduce the calculations. If comparing with FEA software, document the model settings and compare displacement and stress away from local stress concentrations.

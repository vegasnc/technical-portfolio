E = 200000000000.0
L = 0.15
b = 0.02
h = 0.006
F = 100.0

I = b * h**3 / 12
max_nominal_bending_stress_pa = 6 * F * L / (b * h**2)
tip_deflection_m = F * L**3 / (3 * E * I)

print(f"Second moment of area: {I:.6e} m^4")
print(f"Nominal bending stress: {max_nominal_bending_stress_pa / 1e6:.2f} MPa")
print(f"Tip deflection: {tip_deflection_m * 1e3:.3f} mm")

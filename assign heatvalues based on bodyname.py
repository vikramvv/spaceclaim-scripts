"""
Heat Source Assignment Script for Ansys Discovery

This Python script assigns heat sources to different components in an Ansys Discovery model and calculates the total heat generated.

Author: Vikramv
License: MIT License (https://opensource.org/licenses/MIT)

API Version: V21
"""

try:
    # Delete existing heat sources
    for c in Conditions.Heat.GetAll():
        c.Delete()
finally:
    print('Deleted heat sources if any')

# Define power quantities for different components
Transformer_core = PowerQuantity.Create(5, PowerUnit.Watt)
HV_coil = PowerQuantity.Create(2.00 / 2, PowerUnit.Watt)
LV_coil = PowerQuantity.Create(10, PowerUnit.Watt)
Transformer_ind_coil = PowerQuantity.Create(10, PowerUnit.Watt)
Transformer_ind_core = PowerQuantity.Create(10, PowerUnit.Watt)
HVfet_HS = PowerQuantity.Create(10, PowerUnit.Watt)
HVfet_LS = PowerQuantity.Create(10, PowerUnit.Watt)
LVfet_HS = PowerQuantity.Create(10, PowerUnit.Watt)
LVfet_LS = PowerQuantity.Create(10, PowerUnit.Watt)
Icore = PowerQuantity.Create(10, PowerUnit.Watt)
Icoil = PowerQuantity.Create(10, PowerUnit.Watt)
RPE = PowerQuantity.Create(10, PowerUnit.Watt)
PCB = PowerQuantity.Create(10, PowerUnit.Watt)

# Assign values to heat sources based on component names
selection = Selection.Empty()

# Add more components as needed
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('tcore'):
        selection = Selection.Create(c)
        result = Conditions.Heat.Create(selection, Transformer_core)
        result.Label = "Transformer_core"

# (Repeat the above block for other components)

# Calculate the total heat generated
watts = PowerQuantity.Create(0.00, PowerUnit.Watt)
for d in Conditions.Heat.GetAll():
    watts = d.TotalHeat + watts

print('Total heat:', watts)

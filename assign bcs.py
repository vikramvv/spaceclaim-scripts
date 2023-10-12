"""
Heat Source and Temperature Assignment Script for Ansys Discovery

This Python script assigns heat sources to different components and ensures a uniform temperature in an Ansys Discovery model.

Author: vikramv
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
Transformer_core = PowerQuantity.Create(10, PowerUnit.Watt)
Transformer_coil = PowerQuantity.Create(10, PowerUnit.Watt)
HVfet = PowerQuantity.Create(10, PowerUnit.Watt)
LVfet = PowerQuantity.Create(10, PowerUnit.Watt)
RPE = PowerQuantity.Create(10, PowerUnit.Watt)
Icore = PowerQuantity.Create(10, PowerUnit.Watt)
Icoil = PowerQuantity.Create(10, PowerUnit.Watt)

# Define ambient temperature
T_amb_in_C = TemperatureQuantity.Create(80, TemperatureUnit.DegreeCelsius)

# Assign values to heat sources
indexwatt = [Transformer_core, Transformer_coil, HVfet, LVfet, RPE, Icore, Icoil]
selection = Selection.Empty()

# Add more components as needed
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('tcore'):
        selection = Selection.Create(c)
        result = Conditions.Heat.Create(selection, indexwatt[0])
        result.Label = str(c.GetName())

# (Repeat the above block for other components)

# Enable gravity (if needed, uncomment the following section)
# Ensure all temperatures are 80°C
# (Uncomment the remaining sections if needed)

# Include a description of what the script does in a README file.
# Specify the license in a LICENSE file (e.g., MIT License).

# End of the script

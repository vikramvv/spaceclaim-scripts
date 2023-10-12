"""
Transformer Heat Dissipation Analysis Script

This Python script calculates and labels the heat dissipation of different components in a transformer model.
It uses the selected bodies in the 3D model to measure their volume and then calculates the heat dissipation
based on predefined power values for each component.

Author: vikramv
License: MIT License (https://opensource.org/licenses/MIT)

API Version: V21
"""

# Define power values for different components
Transformer_core = 5
HV_coil = 2.00 / 2
LV_coil = 3.5
Transformer_ind_coil = 0.7
Transformer_ind_core = 0.5
HVfet_HS = 3.00
HVfet_LS = 3.00
LVfet_HS = 0.10
LVfet_LS = 5.50
Icore = 0.3
Icoil = 3.9
RPE = 4.80 / 4
PCB = 5.00

# Create an empty selection and secondary selection
selection = Selection.Empty()
secondarySelection = Selection.Empty()

# Initialize an index to keep track of component numbers
index = 1

# Iterate through all bodies in the root part
for c in GetRootPart().GetAllBodies():
    # Check if the body name starts with 'tcore'
    if c.GetName().ToLower().startswith('tcore'):
        selection = Selection.Create(c)
        result = NamedSelection.Create(selection, secondarySelection)
        vol = MeasureHelper.MeasureVolume(selection)
        volheat = round(Transformer_core / vol, 2)
        Lab = f"Transformer_core_{index}_{Transformer_core}W_{volheat}Wm3"
        result = NamedSelection.Rename("Group1", Lab)
        index += 1

# (Repeat the above block for other components)

# Note: Make sure to repeat the above block for other components with appropriate names and power values.

# Include a description of what the script does in a README file.
# Specify the license in a LICENSE file (e.g., MIT License).

# End of the script

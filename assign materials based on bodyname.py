"""
Material Assignment Script for Ansys Discovery

This Python script assigns materials to different components in an Ansys Discovery model. It also sets object visibility for certain components.

Author: vikramv
License: MIT License (https://opensource.org/licenses/MIT)

API Version: V21
"""

from Ansys.Discovery.Api.V21.Solution import Simulation

# Create a reference to the current simulation
s1 = Simulation.GetCurrentSimulation()

# Show all components and invert their visibility
ViewHelper.ShowAll()
ViewHelper.InvertVisibility()

# Define material assignments based on component names
# For each component, assign the appropriate material and set object visibility
# Add more components as needed

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('air'):
        material = Materials.Material.GetLibraryMaterial("Air")
        Materials.MaterialAssignment.Create(s1, d, material)
        print(d.GetName(), material.Label)

# (Repeat the above block for other components)

# Note: Make sure to repeat the above block for other components with appropriate names and materials.

# Include a description of what the script does in a README file.
# Specify the license in a LICENSE file (e.g., MIT License).

# End of the script

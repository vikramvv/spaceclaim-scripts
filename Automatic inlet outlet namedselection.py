"""
Simulation Setup Script for Ansys Discovery

This Python script sets up a simulation in Ansys Discovery with specified conditions, including gravity, temperature, and flow.

Author: vikramv
License: MIT License (https://opensource.org/licenses/MIT)

API Version: V21
"""

## Designed for y axis negative as gravity 
T_amb_in_C = TemperatureQuantity.Create(80, TemperatureUnit.DegreeCelsius)
largestvolume = 0.00000000 
ymax = 0.0000000
ymin = 0.0000000

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('enclosure'):
        print(d.GetName())
        selection = Selection.Create(d)
        vol = round((MeasureHelper.MeasureVolume(selection)), 8)
        if vol >= largestvolume:
            a = BodySelection.Create(d)                
        else:
            largestvolume = vol

for domain in a:
    for face in domain.Faces:
        mdPoint = face.BoundingBox.Center
        if mdPoint[1] >= ymax:
            ymax = mdPoint[1]
            outlet = face
        if mdPoint[1] <= ymin:
            ymin = mdPoint[1]
            inlet = face
            
try:
    for c in Conditions.Flow.GetAll():
        c.Delete()
finally:
    print('Deleted flow conditions if any')

pressure = PressureQuantity.Create(0, PressureUnit.Pascal)
selection = outlet
result = Conditions.Flow.Create(selection, pressure, FlowDirection.Out)
result.Label = "outlet"
selection = inlet
result = Conditions.Flow.Create(selection, pressure, FlowDirection.In)
result.Label = "inlet"

# Enable gravity
try:
    # Change Gravity Component Or Magnitude
    condition = Conditions.Gravity.GetByLabel("Gravity")
    condition.IncludeBuoyancy = True
    condition.GravityAcceleration = Units.VectorQuantityAcceleration.Create(0, -9.81, 0, AccelerationUnit.MeterPerSecondSquared)
        
    # EndBlock
finally:
    print('Gravity was enabled in -z if applicable')

# Ensure all temps are 80°C
for f in Conditions.Flow.GetAll():
    try: 
        f.Temperature = T_amb_in_C
    finally:
        print('fbc')
    
for f in Conditions.FluidInitialTemperature.GetAll():
    try: 
        f.Magnitude = T_amb_in_C
    finally:
        print('fbc')
    
for f in Conditions.Convection.GetAll():
    try: 
        f.ExternalTemperature = T_amb_in_C
    finally:
        print('fbc')

# End of the script

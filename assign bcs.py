# Python Script, API Version = V21
try:
    for c in Conditions.Heat.GetAll():
        c.Delete()
finally:
    print 'Deleted heat sources if any'

Transformer_core=PowerQuantity.Create(10,PowerUnit.Watt)
Transformer_coil=PowerQuantity.Create(10,PowerUnit.Watt)
HVfet=PowerQuantity.Create(10,PowerUnit.Watt)
LVfet=PowerQuantity.Create(10,PowerUnit.Watt)
Icore=PowerQuantity.Create(10,PowerUnit.Watt)
Icoil=PowerQuantity.Create(10,PowerUnit.Watt)
RPE=PowerQuantity.Create(10,PowerUnit.Watt)


T_amb_in_C= TemperatureQuantity.Create(80, TemperatureUnit.DegreeCelsius)

#Assign values to heat sources
indexwatt=[Transformer_core,Transformer_coil,HVfet,LVfet,RPE,Icore,Icoil]
selection = Selection.Empty()
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('tcore'):
       selection =Selection.Create(c)
       result = Conditions.Heat.Create(selection,indexwatt[0])
       result.Label=str(c.GetName())
    if c.GetName().ToLower().startswith('tcoil'):
       selection =Selection.Create(c)
       result = Conditions.Heat.Create(selection,indexwatt[1])
       result.Label=str(c.GetName())
    if c.GetName().ToLower().startswith('hv'):
        selection =Selection.Create(c)
        result = Conditions.Heat.Create(selection,indexwatt[2])
        result.Label=str(c.GetName())
    if c.GetName().ToLower().startswith('lv'):
       selection =Selection.Create(c)
       result = Conditions.Heat.Create(selection,indexwatt[3])
       result.Label=str(c.GetName())
    if c.GetName().ToLower().startswith('rpe'):
        selection =Selection.Create(c)
        result = Conditions.Heat.Create(selection,indexwatt[4])
        result.Label=str(c.GetName())
    if c.GetName().ToLower().startswith('icore'):
       selection =Selection.Create(c)
       result = Conditions.Heat.Create(selection,indexwatt[5])
       result.Label=str(c.GetName())
    if c.GetName().ToLower().startswith('icoil'):
        selection =Selection.Create(c)
        result = Conditions.Heat.Create(selection,indexwatt[6])
        result.Label=str(c.GetName())

'''        
#Enable gravity
try:
   # Change Gravity Component Or Magnitude
    condition = Conditions.Gravity.GetByLabel("Gravity")
    condition.IncludeBuoyancy = True
    condition.GravityAcceleration=Units.VectorQuantityAcceleration.Create(0,-9.81,0,AccelerationUnit.MeterPerSecondSquared)
    condition = Conditions.Convection.GetByLabel("Convection (default)")
    
    # EndBlock
finally:
    print 'gravity was enable in -z if applicable'

#Ensure all temps are 80C
for f in Conditions.Flow.GetAll():
    try: 
        f.Temperature = T_amb_in_C
    finally: print 'fbc'
    
for f in Conditions.FluidInitialTemperature.GetAll():
    try: 
        f.Magnitude = T_amb_in_C
    finally: print 'fbc'
    
for f in Conditions.Convection.GetAll():
    try: 
        f.ExternalTemperature = T_amb_in_C
    finally: print 'fbc'
        
# EndBlock'''
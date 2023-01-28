# Python Script, API Version = V21
from Ansys.Discovery.Api.V21.Solution import Simulation


s1=Simulation.GetCurrentSimulation()
ViewHelper.ShowAll()
ViewHelper.InvertVisibility()

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('air'):
        material = Materials.Material.GetLibraryMaterial("Air")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label
                    
for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('mat_pa6'):
        material = Materials.Material.GetLibraryMaterial("Plastic, PA6")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label           
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show) 

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('mat_kapton'):
        material = Materials.Material.GetLibraryMaterial("Kapton")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label  
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('mat_potting'):
        material = Materials.Material.GetLibraryMaterial("Potting")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label  
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('mat_heat'):
        material = Materials.Material.GetLibraryMaterial("Aluminum alloy, wrought, 6061, T6")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label    
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('mat_copper') or d.GetName().ToLower().Contains('mat_cu'):
        material = Materials.Material.GetLibraryMaterial("Copper, C10100, hard")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label    
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)
        
for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('mat_ferrite') :
        material = Materials.Material.GetLibraryMaterial("Magnet, permanent, Ferrite Y30BH (YBM-2B)")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label    
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('mat_pcb') or d.GetName().ToLower().Contains('pcb'):
        material = Materials.Material.GetLibraryMaterial("PCB laminate, Epoxy/Glass fiber, FR-4")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label    
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('cap') or d.GetName().ToLower().Contains('el') or d.GetName().ToLower().Contains('filter') or d.GetName().ToLower().Contains('carrier'):
        material = Materials.Material.GetLibraryMaterial("Plastic, ABS (high-impact)")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label    
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('sheetmetal'):
        material = Materials.Material.GetLibraryMaterial("aw-5754")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label    
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)
    
for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('glue'):
        material = Materials.Material.GetLibraryMaterial("DOW 7091")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label    
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)
        
for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('mat_al'):
        material = Materials.Material.GetLibraryMaterial("Aluminum alloy, wrought, 6061, T6")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label  
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().startswith('gapfiller') or d.GetName().ToLower().Contains('tim'):
        material = Materials.Material.GetLibraryMaterial("semicosil 9671tc2")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label   
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)

for d in GetRootPart().GetAllBodies():
    if d.GetName().ToLower().Contains('nomex'):
        material = Materials.Material.GetLibraryMaterial("Nomex")
        Materials.MaterialAssignment.Create(s1,d,material)
        print d.GetName(),material.Label   
        ViewHelper.SetObjectVisibility(Selection.Create(d),VisibilityType.Show)

print 'completed'

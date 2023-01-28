# Python Script, API Version = V21
Transformer_core=5
HV_coil=2.00/2
LV_coil=3.5
Transformer_ind_coil=0.7
Transformer_ind_core=0.5
HVfet_HS=3.00
HVfet_LS=3.00
LVfet_HS=0.10
LVfet_LS=5.50
Icore=0.3
Icoil=3.9
RPE=4.80/4
PCB=5.00

selection = Selection.Empty()
secondarySelection = Selection.Empty()
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('tcore'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(Transformer_core/vol,2)
       Lab="Transformer_core_"+str(index)+"_"+str(Transformer_core)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1

for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('hv_coil'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(HV_coil/vol,2)
       Lab="HV_coil"+str(index)+"_"+str(HV_coil)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('lv_coil'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(LV_coil/vol,2)
       Lab="LV_coil"+str(index)+"_"+str(LV_coil)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('t_i_core'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(Transformer_ind_core/vol,2)
       Lab="Transformer_ind_core"+str(index)+"_"+str(Transformer_ind_core)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('t_i_coil'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(Transformer_ind_coil/vol,2)
       Lab="Transformer_ind_coil"+str(index)+"_"+str(Transformer_ind_coil)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('hvfet_hs'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(HVfet_HS/vol,2)
       Lab="HVfet_HS"+str(index)+"_"+str(HVfet_HS)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('hvfet_ls'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(HVfet_LS/vol,2)
       Lab="HVfet_LS"+str(index)+"_"+str(HVfet_LS)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('lvfet_hs'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(LVfet_HS/vol,2)
       Lab="LVfet_HS"+str(index)+"_"+str(LVfet_HS)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('lvfet_ls'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(LVfet_LS/vol,2)
       Lab="LVfet_LS"+str(index)+"_"+str(LVfet_LS)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('rpe'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(RPE/vol,2)
       Lab="RPE"+str(index)+"_"+str(RPE)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('icore'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(Icore/vol,2)
       Lab="Icore"+str(index)+"_"+str(Icore)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('icoil'):
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(Icoil/vol,2)
       Lab="Icoil"+str(index)+"_"+str(Icoil)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('pcb_cu') or c.GetName().ToLower().startswith('pcb') :
       selection =Selection.Create(c)
       result = NamedSelection.Create(selection, secondarySelection)
       vol=MeasureHelper.MeasureVolume(selection)
       volheat=round(PCB/vol,2)
       Lab="PCB"+str(index)+"_"+str(PCB)+"W_"+str(volheat)+"Wm3"
       result = NamedSelection.Rename("Group1", Lab)
       index+=1
index=1
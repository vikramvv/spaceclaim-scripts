# Python Script, API Version = V21
try:
    for c in Conditions.Heat.GetAll():
        c.Delete()
finally:
    print 'Deleted heat sources if any'
    
#Transformer_coil=PowerQuantity.Create(9.10,PowerUnit.Watt)
Transformer_core=PowerQuantity.Create(5,PowerUnit.Watt)
HV_coil=PowerQuantity.Create(2.00/2,PowerUnit.Watt)
LV_coil=PowerQuantity.Create(10,PowerUnit.Watt)
Transformer_ind_coil=PowerQuantity.Create(10,PowerUnit.Watt)
Transformer_ind_core=PowerQuantity.Create(10,PowerUnit.Watt)

HVfet_HS=PowerQuantity.Create(10,PowerUnit.Watt)
HVfet_LS=PowerQuantity.Create(10,PowerUnit.Watt)
LVfet_HS=PowerQuantity.Create(10,PowerUnit.Watt)
LVfet_LS=PowerQuantity.Create(10,PowerUnit.Watt)
Icore=PowerQuantity.Create(10,PowerUnit.Watt)
Icoil=PowerQuantity.Create(10,PowerUnit.Watt)
RPE=PowerQuantity.Create(10,PowerUnit.Watt)
PCB=PowerQuantity.Create(10,PowerUnit.Watt)


#Assign values to heat sources

selection = Selection.Empty()
for c in GetRootPart().GetAllBodies():
    if c.GetName().ToLower().startswith('tcore'):
       selection =Selection.Create(c)
       result = Conditions.Heat.Create(selection,Transformer_core)
       result.Label="Transformer_core"

    if c.GetName().ToLower().startswith('hv_coil'):
       selection =Selection.Create(c)
       result = Conditions.Heat.Create(selection,HV_coil)
       result.Label="HV_coil"

    if c.GetName().ToLower().startswith('lv_coil'):
       selection =Selection.Create(c)
       result = Conditions.Heat.Create(selection,LV_coil)
       result.Label="LV_coil"

    if c.GetName().ToLower().startswith('t_i_core'):
       selection =Selection.Create(c)
       result = Conditions.Heat.Create(selection,Transformer_ind_core)
       result.Label="Transformer_ind_core"

    if c.GetName().ToLower().startswith('t_i_coil'):
       selection =Selection.Create(c)
       result = Conditions.Heat.Create(selection,Transformer_ind_coil)
       result.Label="Transformer_ind_coil"

    if c.GetName().ToLower().startswith('hvfet_hs'):
        selection =Selection.Create(c)
        result = Conditions.Heat.Create(selection,HVfet_HS)
        result.Label="HVfet_HS"

    if c.GetName().ToLower().startswith('hvfet_ls'):
        selection =Selection.Create(c)
        result = Conditions.Heat.Create(selection,HVfet_LS)
        result.Label="HVfet_LS"

    if c.GetName().ToLower().startswith('lvfet_hs'):
        selection =Selection.Create(c)
        result = Conditions.Heat.Create(selection,LVfet_HS)
        result.Label="LVfet_HS"

    if c.GetName().ToLower().startswith('lvfet_ls'):
       selection =Selection.Create(c)
       result = Conditions.Heat.Create(selection,LVfet_LS)
       result.Label="LVfet_LS"

    if c.GetName().ToLower().startswith('rpe'):
        selection =Selection.Create(c)
        result = Conditions.Heat.Create(selection,RPE)
        result.Label="RPE"

    if c.GetName().ToLower().startswith('icore'):
       selection =Selection.Create(c)
       result = Conditions.Heat.Create(selection,Icore)
       result.Label="inductor_core"

    if c.GetName().ToLower().startswith('icoil'):
        selection =Selection.Create(c)
        result = Conditions.Heat.Create(selection,Icoil)
        result.Label="inductor_coil"

    if c.GetName().ToLower().startswith('pcb_cu_top') or c.GetName().ToLower().startswith('pcb_cu_bot') :
        selection =Selection.Create(c)
        result = Conditions.Heat.Create(selection,PCB)
        #result.Label=str(c.GetName())
        result.Label="pcb"

#watts=PowerQuantity.Create(0.00,PowerUnit.Watt)
#watts=Transformer_coil+Transformer_core+Icoil+Icore+HVfet+LVfet+RPE+HVfet+LVfet+RPE+HVfet+LVfet+RPE+HVfet+LVfet+RPE+Icoil+Icore
#print 'actual conditions :',watts
watts=PowerQuantity.Create(0.00,PowerUnit.Watt)
for d in Conditions.Heat.GetAll():
    watts=d.TotalHeat+watts
print 'Totalheat: ',watts
# Python Script, API Version = V23

# Simplify Object
result = FixExtraEdges.FindAndFix(Info5)
# EndBlock
secondarySelection = Selection.Empty()
# Imprint Curves
options = FixImprintOptions()
options.Tolerance = MM(0.1)
options.SearchFaces = True
options.SearchEdges = True
options.SearchCurves = True
options.ImprintInstanceType = ImprintInstanceType.IgnoreInstances
result = FixImprint.FindAndFix(options, Info5)
# EndBlock

imprintface=FaceSelection.Create(ImprintEdgesResult(success,Info5).CreatedFaces)
result = NamedSelection.Create(imprintface.FilterMinArea(), secondarySelection)
result = NamedSelection.Rename("Group1", "tt")
# EndBlock
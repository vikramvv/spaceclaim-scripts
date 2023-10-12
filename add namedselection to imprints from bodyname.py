"""
Geometry Simplification and Imprinting Script for Ansys Discovery

This Python script simplifies geometry by fixing extra edges and imprints curves and faces.

Author: vikramv
License: MIT License (https://opensource.org/licenses/MIT)

API Version: V23
"""

# Simplify Object
result = FixExtraEdges.FindAndFix(Info5)

secondarySelection = Selection.Empty()

# Imprint Curves
options = FixImprintOptions()
options.Tolerance = MM(0.1)
options.SearchFaces = True
options.SearchEdges = True
options.SearchCurves = True
options.ImprintInstanceType = ImprintInstanceType.IgnoreInstances
result = FixImprint.FindAndFix(options, Info5)

# Create a named selection for the imprinted faces
imprintface = FaceSelection.Create(ImprintEdgesResult(success, Info5).CreatedFaces)
result = NamedSelection.Create(imprintface.FilterMinArea(), secondarySelection)
result = NamedSelection.Rename("Group1", "tt")

# Include a description of what the script does in a README file.
# Specify the license in a LICENSE file (e.g., MIT License).

# End of the script

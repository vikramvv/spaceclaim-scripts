# Python Script, API Version = V22

# Create a point at coordinates (0, 0, 0)
p1 = Point.Create(0, 0, 0)

# Create another point at (1, 0, 0) which can be considered as the axis of rotation
p2 = Point.Create(1, 0, 0)  # Change to the required axis of rotation

# Create a line that passes through points p1 and p2
l1 = Line.CreateThroughPoints(p1, p2)

# Activate a named view called "Trimetric" with scale factors of 1 for both axis
ViewHelper.ActivateNamedView("Trimetric", 1, 1)

# Get the current projection view, which is assumed to be the Trimetric view
view1 = ViewHelper.GetCurrentProjection()  # view1 is Trimetric

# Rotate the view (view1) by 30 degrees around the line l1
o1 = view1 * Matrix.CreateRotation(l1, 30)  # 30 degrees

# Rotate the previously rotated view (o1) by an additional 60 degrees around the line l1
o2 = o1 * Matrix.CreateRotation(l1, 60)  # 60 degrees

# Set the projection view to the final rotated view (o2) with scale factors of 1 for both axes
ViewHelper.SetProjection(o2, 1, 1)

# Set the projection view back to the intermediate rotated view (o1) with scale factors of 1 for both axes
ViewHelper.SetProjection(o1, 1, 1)

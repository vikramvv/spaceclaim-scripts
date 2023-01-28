# Python Script, API Version = V22
p1=Point.Create(0,0,0)
p2=Point.Create(1,0,0)# change to required axis of rotation
l1=Line.CreateThroughPoints(p1,p2)
ViewHelper.ActivateNamedView("Trimetric",1,1)
view1=ViewHelper.GetCurrentProjection() #view1 is trimetric
o1=view1*Matrix.CreateRotation(l1,30) #30deg
o2=o1*Matrix.CreateRotation(l1,60) # 60deg 
ViewHelper.SetProjection(o2,1,1)
ViewHelper.SetProjection(o1,1,1)

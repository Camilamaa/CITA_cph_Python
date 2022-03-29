import rhinoscriptsyntax as rs
points = rs.GetPointCoordinates("Select points")

a = min(points)
start = a

while a:
    b = a
    a = points[0]
    for c in points:
        if (a[0]-b[0])*(c[1]-b[1])-(a[1]-b[1])*(c[0]-b[0]) < 0: a = c
    rs.AddLine(b,a)
    
    if a == start: break
    
    
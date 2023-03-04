from objects import *
import matplotlib.pyplot as plt
import settings as s
from figure import Figure


p1, p2, p3 = (Point(-0.7 - 0.8j), Point(-0.5 + 0.6j), Point(0.9 + 0.2j))
l1, l2, l3 = LineSegment(p1, p2), LineSegment(p2, p3), LineSegment(p3, p1)
m1, m2, m3 = MidPoint(p1, p2), MidPoint(p2, p3), MidPoint(p3, p1)
pd1, pd2, pd3 = (
    Perpendicular(l1, m1, style=s.PERPENDICULAR_STYLE),
    Perpendicular(l2, m2, style=s.PERPENDICULAR_STYLE),
    Perpendicular(l3, m3, style=s.PERPENDICULAR_STYLE),
)
intersect = Intersect(pd1, pd2)

circ = Circ(intersect, p1)

fig = Figure(p1, p2, p3, circ, l1, l2, l3, pd1, pd2, pd3)
plt.show()

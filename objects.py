import numpy as np
from graphics import Graphics
import settings as s
import matplotlib.patches as pat
import matplotlib.lines as lines
import matplotlib.pyplot as plt


class Point(Graphics):
    is_dragable = True

    def __init__(self, pos: complex, **kwargs) -> None:
        self.pos = pos
        self.init_style(**kwargs)

    def init_style(self, color=s.POINT_COLOR, plot_radius=s.POINT_RADIUS):
        self.color = color
        self.plot_radius = plot_radius

    def set_to(self, new_pos: complex):
        self.pos = new_pos
        pass

    def __call__(self) -> complex:
        return self.pos

    def _get_artist(self):
        point_coords = self()
        return pat.Circle(
            (point_coords.real, point_coords.imag), self.plot_radius, color=self.color
        )


class Line(Graphics):
    is_dragable = False

    def __init__(self, point1: Point, point2: Point, **kwargs) -> None:
        self.point1 = point1
        self.point2 = point2
        self.init_style(**kwargs)

    def init_style(self, color=s.LINE_COLOR, style="-"):
        self.color = color
        self.style = style

    def __call__(self) -> tuple[complex, complex]:
        """(point, vector)"""
        return (self.point1(), self.point2() - self.point1())

    def _get_artist(self):
        point, vec = self()
        point2 = point + vec
        return plt.axline(
            [point.real, point.imag],
            [point2.real, point2.imag],
            color=self.color,
            linestyle=self.style,
        )


class LineSegment(Line):
    def __init__(self, point1: Point, point2: Point, **kwargs):
        super(LineSegment, self).__init__(point1, point2, *kwargs)

    def _get_artist(self):
        p1 = self.point1()
        p2 = self.point2()
        return lines.Line2D(
            [p1.real, p2.real],
            [p1.imag, p2.imag],
            s.LINE_WIDTH,
            color=s.LINE_COLOR,
        )


class MidPoint(Point):
    def __init__(self, point1: Point, point2: Point, **kwargs) -> None:
        self.point1 = point1
        self.point2 = point2
        self.init_style(**kwargs)

    def __call__(self) -> complex:
        return (self.point1() + self.point2()) / 2


class Perpendicular(Line):
    def __init__(self, line: Line, point: Point, **kwargs) -> None:
        self.line = line
        self.point = point
        self.init_style(**kwargs)

    def __call__(self) -> tuple[complex, complex]:
        return (self.point(), self.line()[1] * 1j)


class Intersect(Point):
    def __init__(self, line1: Line, line2: Line, **kwargs) -> None:
        self.line1 = line1
        self.line2 = line2
        self.init_style(**kwargs)

    def __call__(self) -> complex:
        a, v = self.line1()
        b, w = self.line2()

        return b + w * ((a - b) * v.conjugate()).imag / (w * v.conjugate()).imag


class Circ(Graphics):
    is_dragable = False

    def __init__(self, midpoint: Point, edgepoint: Point) -> None:
        self.midpoint = midpoint
        self.edgepoint = edgepoint

    def __call__(self) -> tuple[complex, float]:
        """midpoint, radius"""
        return (self.midpoint(), np.abs(self.midpoint() - self.edgepoint()))

    def _get_artist(self):
        point_coords, radius = self()
        return pat.Circle(
            (point_coords.real, point_coords.imag),
            radius,
            color=s.LINE_COLOR,
            fill=False,
        )

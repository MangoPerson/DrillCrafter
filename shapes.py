import math

from drill_objects import DrillShape, DrillPosition


class Dot(DrillShape):
    def __init__(self, performer: str, pos: DrillPosition):
        super().__init__(performer)
        self.positions = [pos]

    @staticmethod
    def from_str(performer: str, pos: str):
        return Dot(performer, DrillPosition.from_str(pos))


class Line(DrillShape):
    start: DrillPosition
    end: DrillPosition

    def __init__(self, performers_str: str, start: DrillPosition, end: DrillPosition):
        super().__init__(performers_str)
        self.start = start
        self.end = end

        self.positions = [start * t + end * (1 - t) for t in self.t_vals()]

    @staticmethod
    def from_str(performers_str: str, start_str: str, end_str: str):
        start = DrillPosition.from_str(start_str)
        end = DrillPosition.from_str(end_str)

        return Line(performers_str, start, end)


class Arc(DrillShape):
    start: DrillPosition
    end: DrillPosition

    def __init__(self, performers_str: str, start: DrillPosition, end: DrillPosition, mid: DrillPosition):
        super().__init__(performers_str)
        self.start = start
        self.end = end

        # slopes
        m1 = (start.vertical - mid.vertical) / (start.horizontal - mid.horizontal)
        m2 = (end.vertical - mid.vertical) / (end.horizontal - mid.horizontal)

        if m1 == m2:
            line = Line(performers_str, start, end)
            self.positions = line.positions
            return

        # midpoints
        mp1 = (start + mid) / 2
        mp2 = (end + mid) / 2

        center_x = (mp2.horizontal / m2 - mp1.horizontal / m1 + end.vertical / 2 - start.vertical / 2) / (1 / m2 - 1 / m1)
        center_y = -1 / m1 * (center_x - mp1.horizontal) + mp1.vertical
        center = DrillPosition(center_x, center_y)

        def angle(u, v):
            return math.acos((u.horizontal * v.horizontal + u.vertical * v.vertical) / (abs(u) * abs(v)))

        def cross(u, v):
            return u.horizontal * v.vertical - u.vertical * v.horizontal

        def rotate(u, theta):
            return DrillPosition(math.cos(theta), math.sin(theta)) * u.horizontal + DrillPosition(-math.sin(theta), math.cos(theta)) * u.vertical

        center_angle = angle(start - center, end - center)
        mid_angle = angle(start - mid, end - mid)

        center_cross = cross(start - center, end - center)

        if mid_angle < math.pi/2:
            arc_angle = math.copysign(center_angle, center_cross) - math.copysign(math.tau, center_cross)
        else:
            arc_angle = math.copysign(center_angle, center_cross)

        self.positions = [rotate(start - center, arc_angle * t) + center for t in self.t_vals()]

    @staticmethod
    def from_str(performers_str: str, start_str: str, end_str: str, mid_str: str):
        start = DrillPosition.from_str(start_str)
        end = DrillPosition.from_str(end_str)
        mid = DrillPosition.from_str(mid_str)

        return Arc(performers_str, start, end, mid)

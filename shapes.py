from drill_objects import DrillShape, DrillPosition


class Dot(DrillShape):
    def __init__(self, performer: str, pos: str):
        super().__init__(performer)
        self.positions = [DrillPosition.from_str(pos)]


class Line(DrillShape):
    start: DrillPosition
    end: DrillPosition

    def __init__(self, performers_str: str, start_str: str, end_str: str):
        super().__init__(performers_str)
        self.start = DrillPosition.from_str(start_str)
        self.end = DrillPosition.from_str(end_str)

        t_vals = [t / (len(self.performers) - 1) for t in range(len(self.performers))]

        self.positions = [self.start * t + self.end * (1 - t) for t in t_vals]

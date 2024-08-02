import re

from drill_objects import DrillShape, DrillSet
from shapes import Dot, Line


def parse_drill_shape(string: str) -> DrillShape:
    if 'LINE' in string:
        performers, start, end = re.split(' LINE | TO ', string)
        return Line(performers, start, end)
    elif 'DOT' in string:
        performer, pos, = string.split(' DOT ')
        return Dot(performer, pos)
    else:
        pass


def parse_drill_set(counts, string: str) -> DrillSet:
    textlines = string.split('\n')
    shapes = [parse_drill_shape(line) for line in textlines if line.strip()]

    return DrillSet(counts, shapes)

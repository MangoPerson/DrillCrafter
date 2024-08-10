import re

from drill_objects import DrillShape, DrillSet
from shapes import Dot, Line, Arc


def parse_drill_shape(string: str) -> DrillShape:
    if 'DOT' in string:
        performer, pos = string.split(' DOT ')
        return Dot.from_str(performer, pos)
    elif 'LINE' in string:
        performers, start, end = re.split(' LINE | TO ', string)
        return Line.from_str(performers, start, end)
    elif 'ARC' in string:
        performers, start, end, mid = re.split(' ARC | TO | THRU ', string)
        return Arc.from_str(performers, start, end, mid)
    else:
        pass


def parse_drill_set(string: str) -> DrillSet:
    textlines = string.split('\n')
    shapes = [parse_drill_shape(line) for line in textlines if line.strip()]

    return DrillSet(shapes)


def parse_drill_file(string: str) -> list[DrillSet]:
    textlines = string.split('\n')
    splits = []
    for line in textlines:
        if re.match('[0-9]+:', line):
            splits += [line]

    reg = '|'.join(splits)

    set_strs = re.split(reg, string)
    sets = [parse_drill_set(set_str.strip()) for set_str in set_strs if set_str.strip()]

    return sets

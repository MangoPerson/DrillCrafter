class DrillFormatException(Exception):
    pass


class DrillPosition:
    horizontal: float
    vertical: float

    @staticmethod
    def from_str(string: str):
        string = string.replace(' ', '')
        lr_str, fb_str = string.split(',')

        if '<' in lr_str:
            [steps_str, yardline_str] = lr_str.split('<')
            steps = -float(steps_str)
        elif '>' in lr_str:
            [steps_str, yardline_str] = lr_str.split('>')
            steps = float(steps_str)
        else:
            steps = 0
            yardline_str = lr_str

        yardline = int(yardline_str.replace('R', '').replace('L', ''))

        if yardline_str.startswith('L'):
            horizontal = -8 / 5 * (50 - yardline) + steps
        else:
            horizontal = 8 / 5 * (50 - yardline) + steps

        if '^' in fb_str:
            [steps_str, line_str] = fb_str.split('^')
            steps = float(steps_str)
        elif 'v' in fb_str:
            [steps_str, line_str] = fb_str.split('v')
            steps = -float(steps_str)
        else:
            steps = 0
            line_str = fb_str

        if line_str == 'HS':
            line = 0
        elif line_str == 'HH':
            line = 28
        elif line_str == 'VH':
            line = 56
        elif line_str == 'VS':
            line = 84
        else:
            raise DrillFormatException('Front-back line must be one of: HS, HH, VH, VS')

        vertical = line + steps

        return DrillPosition(horizontal, vertical)

    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    def __add__(self, other):
        return DrillPosition(self.horizontal + other.horizontal, self.vertical + other.vertical)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return DrillPosition(other * self.horizontal, other * self.vertical)

    def __neg__(self):
        return DrillPosition(-self.horizontal, -self.vertical)

    def __truediv__(self, other):
        return DrillPosition(self.horizontal / other, self.vertical / other)

    def __abs__(self):
        return (self.vertical ** 2 + self.horizontal ** 2) ** (1 / 2)


class DrillShape:
    performers: list[str]
    positions: list[DrillPosition]

    def t_vals(self):
        if len(self.performers) == 1:
            return [0]
        else:
            return [t / (len(self.performers) - 1) for t in range(len(self.performers))]

    def __init__(self, performers_str):
        def parse_numbers(num_string: str):
            num_string = num_string.strip()
            if ',' in num_string:
                result = []
                for part in num_string.split(','):
                    result += parse_numbers(part)
                return result
            elif '-' in num_string:
                bound1, bound2 = num_string.split('-')
                bound1, bound2 = int(bound1), int(bound2)
                step = -1 if bound1 > bound2 else 1
                return list(range(int(bound1), int(bound2) + step, step))
            else:
                return [int(num_string)]

        string = performers_str.strip()
        result = []
        for group in string.split(' '):
            group = group.strip()

            if '(' in group:
                symbol, numstr = group.replace(')', '').split('(')
                numbers = parse_numbers(numstr)
                result += [f'{symbol}{number}' for number in numbers]
            elif len(group) > 0:
                result += [group]

        self.performers = result


class DrillSet:
    shapes: list[DrillShape]

    def __init__(self, shapes: list[DrillShape]):
        self.shapes = shapes

    def get_all_performers(self):
        performers = []
        for shape in self.shapes:
            performers += shape.performers

        return performers

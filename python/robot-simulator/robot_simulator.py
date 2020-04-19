NORTH = {
    'moves': {'L': 'WEST', 'R': 'EAST'},
    'coord': (0, 1),
}
EAST = {
    'moves': {'L': 'NORTH', 'R': 'SOUTH'},
    'coord': (1, 0),
}
SOUTH = {
    'moves': {'L': 'EAST', 'R': 'WEST'},
    'coord': (0, -1),
}
WEST = {
    'moves': {'L': 'SOUTH', 'R': 'NORTH'},
    'coord': (-1, 0),
}


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = (x, y)

    def add_tuples(self, tuple1, tuple2):
        return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]

    def move(self, instruction):
        instruction = [i for i in instruction]
        for move in instruction:
            if move != 'A':
                self.direction = globals()[self.direction['moves'][move]]
            else:
                self.coordinates = self.add_tuples(
                    self.coordinates,
                    self.direction['coord']
                )

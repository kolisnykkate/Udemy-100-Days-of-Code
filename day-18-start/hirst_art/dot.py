
class Dot:
    def __init__(self, radius, distance, wall_distance):
        self.radius = radius
        self.distance = distance
        self.wall_distance = wall_distance


    def dot_num(self, total_length,):
        dots = int((total_length - (self.wall_distance - self.distance / 2) * 2) / self.distance)
        return dots




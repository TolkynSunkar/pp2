class Ball:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.radius = 25
        self.step = 20

    def move(self, dx, dy, width, height):
        new_x = self.x + dx * self.step
        new_y = self.y + dy * self.step

        if self.radius <= new_x <= width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= height - self.radius:
            self.y = new_y
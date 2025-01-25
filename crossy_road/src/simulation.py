import pyxel


class Pedestrian:
    def __init__(self, y):
        self.y = y
        self.w = 10
        self.h = 10
        self.v = 5

class Car:
    def __init__(self, x):
        self.x = x
        self.w = 50
        self.h = 10
        self.v = 20

class App:
    def __init__(self):
        pyxel.init(
            width=700,
            height=700,
            title="road crossing simulation",
            fps=6,
            display_scale=1
        )
        self.p = Pedestrian(pyxel.height)
        self.c = Car(0)
        self.a = 200
        self.b = pyxel.height - self.a

        pyxel.run(self.update, self.draw)

    def update(self):
        self.move_pedestrian()
        self.move_car()
    
    def move_pedestrian(self):
        if self.p.y == 0:
            return
        self.p.y -= self.p.v
    
    def move_car(self):
        if self.c.x == pyxel.width:
            return
        self.c.x += self.c.h

    def draw(self):
        pyxel.cls(0)
        self.draw_background()
        self.draw_pedestrian()
        self.draw_car()

    def draw_background(self):
        # darker cyan background
        pyxel.rect(x=0, y=0, w=pyxel.width, h=pyxel.height, col=3)
        # lighter cyan background
        pyxel.rect(x=0, y=0, w=pyxel.width, h=self.b, col=11)

        # bottom and upper sidewalk
        pyxel.rect(x=0, y=pyxel.height - 10, w=pyxel.width, h=10, col=4)
        pyxel.rect(x=0, y=0, w=pyxel.width, h=10, col=4)

        # guideline
        pyxel.rect(x=(pyxel.width / 2) - 5, y=0, w=10, h=pyxel.height, col=2)

    def draw_pedestrian(self):
        pyxel.rect(
            x=(pyxel.width / 2) - 5, 
            y=self.p.y, 
            w=self.p.w, 
            h=self.p.h, 
            col=9
        )

    def draw_car(self):
        pyxel.rect(
            x=self.c.x - self.c.w,
            y=(pyxel.height / 2) - 5,
            w=self.c.w,
            h=self.c.h,
            col=1
        )


App()

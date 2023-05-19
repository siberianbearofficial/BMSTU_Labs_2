from random import randint, choice

import pygame as pg

from figures.asteroids.asteroid1 import Asteroid1
from figures.asteroids.asteroid2 import Asteroid2
from figures.asteroids.asteroid3 import Asteroid3

from lab5.figures.star import Star
from lab5.figures.space_craft import SpaceCraft


FPS = 60


class Window:
    def __init__(self):
        self.step = 0
        self.screen = pg.display.set_mode((800, 1000))
        self.space_craft = None
        self.asteroids = None
        self.stars = None
        self.restart()

    def restart(self):
        self.step = 0
        self.space_craft = SpaceCraft(550, 1080)
        self.space_craft.rotate(-0.5)
        self.space_craft.speed = (-0.5, -1)
        self.space_craft.acceleration = (0, -0.001)

        self.asteroids = [
            Asteroid1(50, -50).set_speed(0.001, 1).set_rotation_angle(0.003),
            Asteroid2(600, -100).set_speed(-0.01, 1.5).set_rotation_angle(-0.008),
            Asteroid3(150, -500).set_speed(0.1, 0.5).set_rotation_angle(0.001),
            Asteroid3(0, 850).set_speed(-0.005, 0.5).set_rotation_angle(-0.001),
        ]

        self.stars = [
            Star(randint(0, 800), randint(-1000, 1000))
            .set_speed(0, 0.05)
            .set_rotation_angle(0.001 * choice((-1, 1)))
            for _ in range(100)
        ]

    def update(self):
        self.step += 1

        # Asteroids
        i = 0
        for asteroid in self.asteroids:
            asteroid.update_pos()
            asteroid.rotate()
            i += 1

        # Stars
        for star in self.stars:
            star.update_pos()
            star.rotate()

        # SpaceCraft
        self.space_craft.update_pos()
        if 1 <= self.step <= 600:
            self.space_craft.rotate(0.001)
        elif 601 <= self.step <= 680:
            self.space_craft.rotate(-0.01)
            self.space_craft.acceleration = (-0.08, -0.08)
        elif 681 <= self.step <= 900:
            self.space_craft.rotate(0.003)
            self.space_craft.acceleration = (0.01, 0.01)

        if self.step == 1000:
            self.restart()

        print(f'\rStep: {self.step} / 2000', end='')
        self.draw()

    def draw(self):
        # Background
        self.screen.fill("#081338")

        # Star
        for star in self.stars:
            for obj in star.objects():
                self.draw_obj(obj)

        # Asteroid
        for asteroid in self.asteroids:
            for obj in asteroid.objects():
                self.draw_obj(obj)

        # SpaceCraft
        for obj in self.space_craft.objects():
            self.draw_obj(obj)

    def draw_obj(self, obj):
        match obj.__class__.__name__:
            case 'Polygon':
                pg.draw.polygon(self.screen, obj.bg_color, list(map(tuple, obj.points)))
                if obj.border_color:
                    pg.draw.polygon(self.screen, obj.border_color, list(map(tuple, obj.points)), 3)
            case 'Circle':
                pg.draw.circle(self.screen, obj.color, tuple(obj.center), obj.radius)
            case 'Line':
                pg.draw.line(self.screen, obj.color, tuple(obj.p1), tuple(obj.p2), 3)


def main():
    pg.init()
    clock = pg.time.Clock()
    window = Window()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(0)
        window.update()
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()

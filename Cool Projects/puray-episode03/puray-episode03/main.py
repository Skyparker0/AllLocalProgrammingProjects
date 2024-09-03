#!/usr/bin/env python
"""Puray - a Pure Python Raytracer by Arun Ravindran, 2019"""
from color import Color
from engine import RenderEngine
from point import Point
from scene import Scene
from sphere import Sphere
from vector import Vector


def main():
    WIDTH = 500
    HEIGHT = 500
    camera = Vector(0.5, -1, -10)
    objects = [Sphere(Point(0, 0, 0), 0.5, Color.from_hex("#FF0000")), 
               Sphere(Point(0, 0.5, 0), 0.5, Color.from_hex("#00FF00")),
               Sphere(Point(0, -0.5, 0), 0.5, Color.from_hex("#0000FF")),
               Sphere(Point(0, 100, 0), 99, Color.from_hex("#999999"))]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()

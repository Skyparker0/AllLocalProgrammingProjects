# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:07:51 2020

@author: batte
"""

import numpy as np
from PIL import Image
from importlib import reload  

Image = reload(Image)


class V:
    
    def __init__(self, point):
        self.array = np.array(point)
        
    def get_array(self):
        return self.array
        
    def magnitude(self):
        return (sum(self.array ** 2))**0.5
    
    def normalize(self):
        return V(self.array / self.magnitude())
    
    def dotProduct(self, other):
        return sum(self.array * other.get_array())
    
    def __str__(self):
        return str(tuple(self.array))
    
    def __add__(self,other):
        return V(self.array + other.array)
    
    def __sub__(self,other):
        return V(self.array - other.array)
    
    def __mul__(self, num):
        return V(self.array * num)
    
    def __rmul__(self, num):
        return V(self.array * num)
    
    def __truediv__(self,num):
        return V(self.array / num)
    
    def c(self):
        return tuple([int(x) for x in np.around(self.array * 255)])

class C(V):
    pass


class Point(V):
    pass

class Ray:
    """Ray is a half-line with an origin and a normalized direction"""

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()
        
class Scene:
    """Scene has all the information needed for the ray tracing engine"""

    def __init__(self, camera, objects, width, height):
        self.camera = camera
        self.objects = objects
        self.width = width
        self.height = height
        
        
class RenderEngine:
    """Renders 3D objects into 2D objects using ray tracing"""

    def render(self, scene):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height
        x0 = -1.0
        x1 = +1.0
        xstep = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspect_ratio
        y1 = +1.0 / aspect_ratio
        ystep = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image.new("RGB",(width,height))

        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep
                ray = Ray(camera, Point([x, y,0]) - camera)
                pixels.putpixel((i, j), self.ray_trace(ray, scene).c())
        return pixels
    
    def ray_trace(self, ray, scene):
        color = C([0, 0, 0])
        # Find the nearest object hit by the ray in the scene
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return color
        hit_pos = ray.origin + ray.direction * dist_hit
        color += self.color_at(obj_hit, hit_pos, scene)
        return color.c()
    
    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj
        return (dist_min, obj_hit)
    
    def color_at(self, obj_hit, hit_pos, scene):
        return obj_hit.material



class Sphere:
    """Sphere is the only 3D shape implemented. Has center, radius and material"""

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        """Checks if ray intersects this sphere. Returns distance to intersection or None if there is no intersection"""
        sphere_to_ray = ray.origin - self.center
        # a = 1
        b = 2 * ray.direction.dotProduct(sphere_to_ray)
        c = sphere_to_ray.dotProduct(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * c

        if discriminant >= 0:
            dist = (-b - np.sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None

def from_hex(hexcolor="#000000"):
    x = int(hexcolor[1:3], 16) / 255.0
    y = int(hexcolor[3:5], 16) / 255.0
    z = int(hexcolor[5:7], 16) / 255.0
    return C([x, y, z])

# class img(Image.new):
    
#     def __init__(self,width,height):
        
#         self.width = width
#         self.height = height
        
#         Image.new.__init__('RGB', (width,height))
        
    
    
    
def main():
    WIDTH = 100
    HEIGHT = 100
    
    camera = V([0,0,0])
    objects = [Sphere(Point([0,0,1]), 0.5, from_hex('#FF0000'))]
    scene = Scene(camera,objects,WIDTH,HEIGHT)
    engine = RenderEngine()
    im = engine.render(scene)
    
    im.show()
    
    im.save("rayTrace.PNG")


if __name__ == "__main__":
    main()
        
        

    
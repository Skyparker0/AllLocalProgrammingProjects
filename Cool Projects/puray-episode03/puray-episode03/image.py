
from PIL import Image as img

class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = img.new("RGB",[width, height])

    def set_pixel(self, x, y, col):
        self.pixels.putpixel([x,y], (round(col.x*255), round(col.y*255), round(col.z*255)))

    def write_ppm(self, img_file):
        # def to_byte(c):
        #     return round(max(min(c * 255, 255), 0))

        # img_file.write("P3 {} {}\n255\n".format(self.width, self.height))
        # for row in self.pixels:
        #     for color in row:
        #         img_file.write(
        #             "{} {} {} ".format(
        #                 to_byte(color.x), to_byte(color.y), to_byte(color.z)
        #             )
        #         )
        #     img_file.write("\n")
        self.pixels.show()
        

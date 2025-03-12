import os
from PIL import Image
import random
import sys
path = os.path.abspath(sys.argv[0])
path = path.replace("pixel_average.py", "")
def get_pixel(image, x, y):
    width, height = image.size
    if(x<0 or x>=width or y<0 or y>=height):
        return (0, 0, 0, 0) if image.mode == 'RGBA' else (0, 0, 0)
    return image.getpixel((x, y))
def average_adjacent_pixels(image):
    width, height = image.size
    new_image = Image.new(image.mode, (width, height))
    for y in range(height):
        for x in range(width):
            if image.mode == 'RGBA':
                ran_avg = random.randint(0,3)
                if(ran_avg==0):
                    r1, g1, b1, a1 = get_pixel(image, x, y)
                elif(ran_avg==1):
                    r1, g1, b1, a1 = get_pixel(image, x-1, y)
                    r2, g2, b2, a2 = get_pixel(image, x+1, y)
                    r3, g3, b3, a3 = get_pixel(image, x, y-1)
                    r4, g4, b4, a4 = get_pixel(image, x, y+1)
                    r = (r1 + r2 + r3 + r4) // 4
                    g = (g1 + g2 + g3 + g4) // 4
                    b = (b1 + b2 + b3 + b4) // 4
                    a = (a1 + a2 + a3 + a4) // 4
                elif(ran_avg==2):
                    r1, g1, b1, a1 = get_pixel(image, x-1, y)
                    r2, g2, b2, a2 = get_pixel(image, x+1, y)
                    r3, g3, b3, a3 = get_pixel(image, x, y-1)
                    r4, g4, b4, a4 = get_pixel(image, x, y+1)
                    r5, g5, b5, a5 = get_pixel(image, x-2, y)
                    r6, g6, b6, a6 = get_pixel(image, x+2, y)
                    r7, g7, b7, a7 = get_pixel(image, x, y-2)
                    r8, g8, b8, a8 = get_pixel(image, x, y+2)
                    r9, g9, b9, a9 = get_pixel(image, x+1, y+1)
                    r10, g10, b10, a10 = get_pixel(image, x-1, y-1)
                    r11, g11, b11, a11 = get_pixel(image, x+1, y-1)
                    r12, g12, b12, a12 = get_pixel(image, x-1, y+1)
                    r = (r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12) // 12
                    g = (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 + g10 + g11 + g12) // 12
                    b = (b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11 + b12) // 12
                    a = (a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12) // 12
                elif(ran_avg==3):
                    r1, g1, b1, a1 = get_pixel(image, x-1, y)
                    r2, g2, b2, a2 = get_pixel(image, x+1, y)
                    r3, g3, b3, a3 = get_pixel(image, x, y-1)
                    r4, g4, b4, a4 = get_pixel(image, x, y+1)
                    r5, g5, b5, a5 = get_pixel(image, x-2, y)
                    r6, g6, b6, a6 = get_pixel(image, x+2, y)
                    r7, g7, b7, a7 = get_pixel(image, x, y-2)
                    r8, g8, b8, a8 = get_pixel(image, x, y+2)
                    r5, g5, b5, a5 = get_pixel(image, x-3, y)
                    r6, g6, b6, a6 = get_pixel(image, x+3, y)
                    r7, g7, b7, a7 = get_pixel(image, x, y-3)
                    r8, g8, b8, a8 = get_pixel(image, x, y+3)
                    r9, g9, b9, a9 = get_pixel(image, x+1, y+1)
                    r10, g10, b10, a10 = get_pixel(image, x-1, y-1)
                    r11, g11, b11, a11 = get_pixel(image, x+1, y-1)
                    r12, g12, b12, a12 = get_pixel(image, x-1, y+1)
                    r13, g13, b13, a13 = get_pixel(image, x+2, y+1)
                    r14, g14, b14, a14 = get_pixel(image, x+1, y+2)
                    r15, g15, b15, a15 = get_pixel(image, x-2, y-1)
                    r16, g16, b16, a16 = get_pixel(image, x-1, y-2)
                    r17, g17, b17, a17 = get_pixel(image, x+2, y-1)
                    r18, g18, b18, a18 = get_pixel(image, x+1, y-2)
                    r19, g19, b19, a19 = get_pixel(image, x-1, y+1)
                    r20, g20, b20, a20 = get_pixel(image, x-1, y+1)
                    r = (r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12 + r13 + r14 + r15 + r16 + r17 + r18 + r19 + r20) // 20
                    g = (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 + g10 + g11 + g12 + g13 + g14 + g15 + g16 + g17 + g18 + g19 + g20) // 20
                    b = (b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11 + b12 + b13 + b14 + b15 + b16 + b17 + b18 + b19 + b20) // 20
                    a = (a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13 + a14 + a15 + a16 + a17 + a18 + a19 + a20) // 20
                new_image.putpixel((x, y), (r, g, b, a))
            else:
                ran_avg = random.randint(0,3)
                if(ran_avg==0):
                    r1, g1, b1 = get_pixel(image, x, y)
                elif(ran_avg==1):
                    r1, g1, b1 = get_pixel(image, x-1, y)
                    r2, g2, b2 = get_pixel(image, x+1, y)
                    r3, g3, b3 = get_pixel(image, x, y-1)
                    r4, g4, b4 = get_pixel(image, x, y+1)
                    r = (r1 + r2 + r3 + r4) // 4
                    g = (g1 + g2 + g3 + g4) // 4
                    b = (b1 + b2 + b3 + b4) // 4
                elif(ran_avg==2):
                    r1, g1, b1 = get_pixel(image, x-1, y)
                    r2, g2, b2 = get_pixel(image, x+1, y)
                    r3, g3, b3 = get_pixel(image, x, y-1)
                    r4, g4, b4 = get_pixel(image, x, y+1)
                    r5, g5, b5 = get_pixel(image, x-2, y)
                    r6, g6, b6 = get_pixel(image, x+2, y)
                    r7, g7, b7 = get_pixel(image, x, y-2)
                    r8, g8, b8 = get_pixel(image, x, y+2)
                    r9, g9, b9 = get_pixel(image, x+1, y+1)
                    r10, g10, b10 = get_pixel(image, x-1, y-1)
                    r11, g11, b11 = get_pixel(image, x+1, y-1)
                    r12, g12, b12 = get_pixel(image, x-1, y+1)
                    r = (r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12) // 12
                    g = (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 + g10 + g11 + g12) // 12
                    b = (b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11 + b12) // 12
                elif(ran_avg==3):
                    r1, g1, b1 = get_pixel(image, x-1, y)
                    r2, g2, b2 = get_pixel(image, x+1, y)
                    r3, g3, b3 = get_pixel(image, x, y-1)
                    r4, g4, b4 = get_pixel(image, x, y+1)
                    r5, g5, b5 = get_pixel(image, x-2, y)
                    r6, g6, b6 = get_pixel(image, x+2, y)
                    r7, g7, b7 = get_pixel(image, x, y-2)
                    r8, g8, b8 = get_pixel(image, x, y+2)
                    r5, g5, b5 = get_pixel(image, x-3, y)
                    r6, g6, b6 = get_pixel(image, x+3, y)
                    r7, g7, b7 = get_pixel(image, x, y-3)
                    r8, g8, b8 = get_pixel(image, x, y+3)
                    r9, g9, b9 = get_pixel(image, x+1, y+1)
                    r10, g10, b10 = get_pixel(image, x-1, y-1)
                    r11, g11, b11 = get_pixel(image, x+1, y-1)
                    r12, g12, b12 = get_pixel(image, x-1, y+1)
                    r13, g13, b13 = get_pixel(image, x+2, y+1)
                    r14, g14, b14 = get_pixel(image, x+1, y+2)
                    r15, g15, b15 = get_pixel(image, x-2, y-1)
                    r16, g16, b16 = get_pixel(image, x-1, y-2)
                    r17, g17, b17 = get_pixel(image, x+2, y-1)
                    r18, g18, b18 = get_pixel(image, x+1, y-2)
                    r19, g19, b19 = get_pixel(image, x-1, y+1)
                    r20, g20, b20 = get_pixel(image, x-1, y+1)
                    r = (r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12 + r13 + r14 + r15 + r16 + r17 + r18 + r19 + r20) // 20
                    g = (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 + g10 + g11 + g12 + g13 + g14 + g15 + g16 + g17 + g18 + g19 + g20) // 20
                    b = (b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11 + b12 + b13 + b14 + b15 + b16 + b17 + b18 + b19 + b20) // 20
    return new_image
# Open an image file
img_path = input("Absolute path to the image = ")
image = Image.open(img_path)
# Adjust pixels to the average of the four adjacent ones
adjusted_image = average_adjacent_pixels(image)
# Save the adjusted image
adjusted_image.save(path+"adjusted_image.png")
# Display the original and adjusted images
image.show()
adjusted_image.show()

'''
Created on May 15, 2015

@author: ghaber
'''
from PIL import Image

def interpolate(start, end, left, right, at):
    return int(float(end - start) / (right - left) * at + start)

def make_gradient(width, height, start, end):
    im = Image.new('RGB', (width, 1))
    data = im.load()
    interpolateL = lambda start, end, at: start + int((end-start) * float(at/width))  # @UnusedVariable
    for item in range(width):
        r = interpolate(start[0], end[0], 0, width, item)
        g = interpolate(start[1], end[1], 0, width, item)
        b = interpolate(start[2], end[2], 0, width, item)
        data[item, 0] = (r,g,b)
    im = im.resize((width, height))
    im.show()
    #im.save('img.png')
        
    
make_gradient(500, 100, (255,255,0), (0,0,255))
make_gradient(1000, 100, (204,119,34), (1,66,37))
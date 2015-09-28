# Use Pillow to render a text file as a PNG
from PIL import ImageFont, ImageDraw, Image

for i in range(100):
    image = Image.new('L', (470,680), color='white')
    
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    text = open(r'C:\Dev\workspace\practice\dailyprogrammer\gol.' + str(i+1)).read()
    
    draw.multiline_text((5,5), text)
    image.save(r'C:\Users\ghaber\Desktop\frame{}.png'.format(i))
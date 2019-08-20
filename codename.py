from PIL import Image, ImageDraw, ImageFont
from words import words
import random

im = Image.new("RGB", (600, 400), (255, 255, 255))
font = ImageFont.truetype('YuGothB.ttc', 14)
draw = ImageDraw.Draw(im)

# 25ワード決定
word = random.sample(words, 25)
print(word)
# カードタイプの決定　0:一般人、1:青陣営、2:赤陣営、3:暗殺者
type = [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,random.randint(1,2)]
random.shuffle(type)
if type.count(1) == 9:
    # blue team start
    start_team = "blue team goes first."
    start_fill = (100, 100, 255)
else:
    # red team start
    start_team = "red team goes first."
    start_fill = (255, 100, 100)
print(type)
print(start_team)

def cards(word, i, j, type):
    if type == 0:
        type_color = (255, 255, 255)
    elif type == 1:
        type_color = (180, 180, 255)
    elif type == 2:
        type_color = (255, 180, 180)
    elif type == 3:
        type_color = (130, 130, 130)

    draw.rectangle((20+110*i, 20+72*j, 20+110*(i+1), 20+72*(j+1)), fill=type_color, outline=(0, 0, 0))
    w,h = draw.textsize(word, font=font)
    draw.multiline_text((20+110*i+55-w/2, 20+72*j+36-h/2), word, fill=(0, 0, 0), font=font)
    return
#draw.line((0, im.height, im.width, 0), fill=(255, 0, 0), width=8)
#draw.rectangle((100, 100, 200, 200), fill=(0, 255, 0))
#draw.ellipse((250, 300, 450, 400), fill=(0, 0, 255))
#draw.rectangle((20, 20, 580, 380), fill=(255, 255, 255), outline=(0, 0, 0))

for i in range(0,5):
    for j in range(0,5):
        cards(word[5*i+j], i,j, type[5*i+j])

draw.multiline_text((0, 0), 'codename 0.5', fill=(0, 0, 0), font=font)
draw.rectangle((130, 5, 145, 15), fill=(180, 180, 255), outline=(0, 0, 0))
draw.multiline_text((150, 0), 'blue team', fill=(0, 0, 0), font=font)
draw.rectangle((230, 5, 245, 15), fill=(255, 180, 180), outline=(0, 0, 0))
draw.multiline_text((250, 0), 'red team', fill=(0, 0, 0), font=font)
draw.rectangle((330, 5, 345, 15), fill=(255, 255, 255), outline=(0, 0, 0))
draw.multiline_text((350, 0), 'bystanders', fill=(0, 0, 0), font=font)
draw.rectangle((430, 5, 445, 15), fill=(130, 130, 130), outline=(0, 0, 0))
draw.multiline_text((450, 0), 'assassin', fill=(0, 0, 0), font=font)
draw.multiline_text((450, 385), start_team, fill=start_fill, font=font)
#im.show()
im.save('pillow_iamge_draw.jpg', quality=95)
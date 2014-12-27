#!/usr/bin/env python

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from urllib import urlretrieve
import os

# The co-ordinates
devil_number_xy = (613, 75)
name_xy = (433, 438)
phone_xy = (643, 521)
qr_xy = (65, 302)

# The font-sizes
devil_number_size = 19
name_size = 19
phone_size = 19

# Sample Data
pk = 7
name = u'Shashwot Adhikari'
phone = u'98x11x3333'
devil_number = u'007'

img = Image.open('watermarked_card.jpg')
draw = ImageDraw.Draw(img)
# write devil number
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-ThinItalic.otf'),
                          devil_number_size)
draw.text(devil_number_xy, devil_number, (255, 255, 255), font=font)
# write name
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-Regular.otf'),
                          name_size)
draw.text(name_xy, name, (255, 255, 255), font=font)
# write phone number
font = ImageFont.truetype(os.path.join('fonts', 'Aileron-Regular.otf'),
                          phone_size)
draw.text(phone_xy, phone, (255, 255, 255), font=font)

# download qr
if not os.path.exists('qrs'):
    os.makedirs('qrs')
urlretrieve(
            'http://api.qrserver.com/v1/create-qr-code/?data=http://manutd.org.np/' + devil_number + '&size=160x160&ecc=H&color=ffffff&bgcolor=000',
            os.path.join('qrs', str(pk) + '.png'))
qr = Image.open(os.path.join('qrs', str(pk) + '.png'))
#make qr transparent
qr = qr.convert('RGBA')
data = qr.getdata()
new_data = []
for item in data:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
qr.putdata(new_data)
qr.save(os.path.join('qrs', str(pk) + '.png'))
# write qr to image
img.paste(qr, qr_xy)

if not os.path.exists('sample_cards'):
    os.makedirs('sample_cards')
img.save(os.path.join('sample_cards', str(pk) + '.jpg'))
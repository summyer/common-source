import os, glob
from PIL import Image

size = 128, 128
for file in glob.glob(r'f://img//*.jpg'):
    print(type(file))
    name, ext = os.path.splitext(file)
    img = Image.open(file)
    img.thumbnail(size)
    img.save(name+'.thumbnail','JPEG')

img = Image.open(r'f://img//11.jpg')
img = img.rotate(90)
#img.show()


text = u"这是一段测试文本，test 123。"
print(text)

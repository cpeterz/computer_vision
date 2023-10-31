from PIL import Image,ImageDraw,ImageFont
from IPython.display import display

img = Image.open('face_picture1.jpg')
width, height = img.size
small_img = img.resize((width//2, height//2))

gray_img = small_img.convert('L')

# 在左上角添加位置信息
draw = ImageDraw.Draw(gray_img)
font_size = 50  # 更大的字体大小
font = ImageFont.truetype("arial.ttf", font_size)
text_color = 255  # 白色
location_text = "Processed by PIL"
text_width, text_height = draw.textsize(location_text, font)
text_x = 10  # X坐标
text_y = 10  # Y坐标
draw.text((text_x, text_y), location_text, fill=text_color, font=font)

# img.show()
gray_img.show()
# gray_img.show()



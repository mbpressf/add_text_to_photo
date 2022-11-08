from PIL import Image, ImageDraw, ImageFont
from datetime  import datetime

while True:
    day = str(datetime.now().day)
    month = str(datetime.now().month)
    year = str(datetime.now().year)
    date = day + '.' + month + '.' + year
    name = (input("Введит ФИО --> "))
    image = Image.open(r"C:\\add_text_to_photo_py\\1.jpg")
    font = ImageFont.truetype(r"C:\\add_text_to_photo_py\\ofont.ru_Anastasia.ttf",150)
    font_number = ImageFont.truetype(r'C:\\add_text_to_photo_py\\kztimesnewroman.ttf', 100)
    drawer = ImageDraw.Draw(image)
    drawer.text((400, 1440), name, font=font, fill='white')
    drawer.text((1050, 2850), date, font=font_number, fill='white')
        
    image.show()
    slesh = '\\' + name + '.png'
    
    image.save(r'C:\add_text_to_photo_py\result'+ slesh)
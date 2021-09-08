from PIL import Image, ImageDraw, ImageFont
name_list = "Sgnons jkh jam jbm jkh jcs jjb jam jom jsm jsm jgb jlm jkb jjb jgb jhd jd jd jmp jg".split(" ")

for i in name_list:
    im = Image.open("ganpatibappa.jpeg")
    d = ImageDraw.Draw(im)
    location = (100,100)
    text_color = (500, 500, 500)
    text_size = (100,100)
    font = ImageFont.FreeTypeFont()
    d.text(location, i, fill=text_color,font=font)
    im.save("certificate_"+i+".pdf")    
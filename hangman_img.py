from PIL import Image

number_wrong = []
for x in range(8):
    x = str(x)
    file_name = 'hm' + x + '.png'
    img_open = Image.open(file_name)
    number_wrong.append(img_open)

splash = []
for x in range(7):
    x = str(x)
    file_name = 'title' + x + '.png'
    img_open = Image.open(file_name)
    splash.append(img_open)

import tkinter
from tkinter import *
from random import randint
import time
from PIL import ImageTk, Image
import pyautogui as pg


root = Tk()
width = 950
height = 900
root.geometry(f"{width}x{height}")
canvasHeight = 700
canvasWidth = 700
canvasWidget = Canvas(root, width=canvasWidth, height=canvasHeight)
canvasWidget.grid(row=4, column=1)
#colours = ['red', 'green', 'white', 'black', 'lime', 'brown', 'pink', 'grey', 'violet', 'blue', 'cyan', 'yellow', 'magenta']
colours = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
           'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
           'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
           'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
           'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
           'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
           'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
           'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
           'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
           'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
           'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
           'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
           'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
           'indian red', 'saddle brown', 'sandy brown',
           'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
           'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
           'pale violet red', 'maroon', 'medium violet red', 'violet red',
           'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
           'thistle', 'snow2', 'snow3',
           'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
           'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
           'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
           'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
           'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
           'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
           'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
           'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
           'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
           'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
           'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
           'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
           'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
           'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
           'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
           'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
           'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
           'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
           'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
           'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
           'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
           'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
           'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
           'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
           'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
           'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
           'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
           'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
           'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
           'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
           'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
           'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
           'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
           'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
           'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
           'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
           'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
           'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
           'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
           'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
           'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
           'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
           'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
           'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
           'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
           'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
           'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
           'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
           'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
           'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
           'gray38', 'gray39', 'gray40', 'gray42', 'gray43']


def hide_rootdow():
    root.withdraw()
    root.after(1000, screenshot)


def crop(filename):
    img = Image.open(filename)
    x1 = 166
    y1 = 175
    x2 = x1 + canvasWidth - 20
    y2 = y1 + canvasHeight - 20
    box = (x1, y1, x2, y2)
    img2 = img.crop(box)
    img2.save(filename)


def screenshot():
    # hide_rootdow()
    clean()
    perform()
    random = int(time.time())
    canvasWidget.create_text(78, 23, text=str(
        random), fill="white", font=('Helvetica 15 bold'))
    canvasWidget.create_text(75, 20, text=str(
        random), fill="black", font=('Helvetica 15 bold'))
    filename = "C:\\Users\\Himanshu Lilhore\\Desktop\\python test\\SS\\" + \
        str(random) + ".jpg"
    ss = pg.screenshot(filename)
    root.deiconify()
    crop(filename)
    Label(root, text="Screenshotted & Cropped",
          font=('Times New Roman', 18, 'bold')).grid(row=5, column=1)
    # clean()
    # perform()


def rann():
    return randint(0, 700)


def clean():
    canvasWidget.delete("all")
    canvasWidget.configure(bg="white")


def perform():
    canvasWidget.configure(bg=colours[randint(0, len(colours) - 1)])
    for i in range(1):
        for j in range(randint(1, 2)):
            canvasWidget.create_line(
                rann(), rann(), rann(), rann(), fill=colours[randint(0, len(colours) - 1)], width=randint(200, 400))
        for k in range(randint(1, 2)):
            canvasWidget.create_oval(
                rann(), rann(), rann(), rann(), outline=colours[randint(0, len(colours) - 1)], width=randint(200, 400))
        for l in range(randint(1, 2)):
            canvasWidget.create_arc(
                rann(), rann(), rann(), rann(), fill=colours[randint(0, len(colours) - 1)], width=randint(200, 400), outline=colours[randint(0, len(colours) - 1)], style=tkinter.ARC)
        for jj in range(randint(1, 1)):
            canvasWidget.create_line(
                rann(), rann(), rann(), rann(), fill=colours[randint(0, len(colours) - 1)], width=randint(100, 150))
        for kk in range(randint(1, 1)):
            canvasWidget.create_oval(
                rann(), rann(), rann(), rann(), outline=colours[randint(0, len(colours) - 1)], width=randint(100, 150))
        for ll in range(randint(1, 1)):
            canvasWidget.create_arc(
                rann(), rann(), rann(), rann(), fill=colours[randint(0, len(colours) - 1)], width=randint(100, 150), outline=colours[randint(0, len(colours) - 1)], style=tkinter.ARC)


def changebg():
    canvasWidget.configure(bg=colours[randint(0, len(colours) - 1)])


drawbutton = Button(root, text="Draw", command=perform)
drawbutton.grid(row=0, column=0)
Button(root, text="Change BG", command=changebg).grid(row=2, column=0)
ssbutton = Button(root, text="Take Screenshot", font=('Aerial 11 bold'),
                  background="#aa7bb1", foreground="white", command=screenshot)
ssbutton.grid(row=3, column=0)
Button(root, text="Clear", command=clean).grid(row=1, column=0)

root.mainloop()

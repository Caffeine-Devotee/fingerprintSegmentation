from guizero import App, PushButton, Picture, Text, Waffle, Box, MenuBar
import os
import sys
from tkinter.filedialog import askopenfilename

filename = ""

def select_image():
    global filename
    filename = askopenfilename()
    picture.value = filename
    os.system("python3 src/main_enhancement.py " + filename)
    os.system("pwd")

def image_enhance():
    global filename
    print(filename)
    base=os.path.basename(filename)
    img_name = os.path.splitext(base)
    img_name = str(img_name[0] + img_name[1])
    print(img_name)
    print("here")
    picture1.value = "enhanced/" + img_name

app = App(title = "Image Processing", bg="#ff8787", height=500, width=800, layout = "grid")
menubar = MenuBar(app,
                  toplevel=["File"],
                  options=[[["Upload File", select_image]]])
picture = Picture(app, image="default.png", grid = [0,0])
picture1 = Picture(app, image="default.png", grid = [1,0])
text = Text(app, text="Original", grid = [0,1])
text1 = Text(app, text="Enhanced", grid = [1,1])
box = Box(app, grid=[0,2])
button3 = PushButton(box, command=image_enhance, text = "Enhance", padx = 20 , pady = 30)
app.display()

from random import randint
import os
from PIL import Image,ImageDraw,ImageFont

font = "./Res/dsm.ttf" #change it :V

s_wh = input("Width and Height(W,H): ")
w = int(s_wh.split(",")[0])
h = int(s_wh.split(",")[1])
s_rgb = input("Background color(R,G,B): ")
r = int(s_rgb.split(",")[0])
g = int(s_rgb.split(",")[1])
b = int(s_rgb.split(",")[2])
print(str(w)+"x"+str(h)+" Background:"+str(r)+","+str(g)+","+str(b))
im = Image.new("RGB",(w,h),(r,g,b))
pn = ImageDraw.Draw(im)
s_fxy = input("The position of the text(x,y): ")
f_x = int(s_fxy.split(",")[0])
f_y = int(s_fxy.split(",")[1])
s_frgb = input("The color of the text(r,g,b): ")
f_r = int(s_frgb.split(",")[0])
f_g = int(s_frgb.split(",")[1])
f_b = int(s_frgb.split(",")[2])
s_f = input("What string you want to insert at ("+str(f_x)+","+str(f_y)+")?\n")
sz_f = int(input("What is the size of the font? "))
fts = ImageFont.truetype(font,sz_f)
pn.text((f_x,f_y),s_f,font=fts,fill=(f_r,f_g,f_b))
print("Size "+str(sz_f)+" Text "+s_f+" created at ("+str(f_x)+","+str(f_y)+").")
t = int(input("How many random lines? "))
for i in range(t):
    pn.line([(randint(1,w),randint(1,h)),(randint(1,w),randint(1,h))],fill=(randint(1,255),randint(1,255),randint(1,255)))
print(str(t)+" Lines created.")
t_p = int(input("How many random points? "))
for i in range(t_p):
    pn.point((randint(1,w),randint(1,h)),fill=(randint(1,255),randint(1,255),randint(1,255)))
print(str(t_p)+" Points created.")
sc = input("Filename(etc. test1): ")
im.save("./"+sc+".png", "png")
print("Saved at "+os.path.abspath(".")+"/"+sc+".png")
print("Exiting...")

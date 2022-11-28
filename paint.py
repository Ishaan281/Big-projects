from tkinter import *
import random
from tkinter.filedialog import asksaveasfile,askopenfilename
from PIL import ImageGrab,ImageTk,Image
root=Tk()
root.title("Paint")
root.geometry("800x600")
root.update_idletasks()
color="black"
size=10
eraser_size=3
symetric_drawing=False
workingEraser=False
def save():
	file = asksaveasfile(defaultextension=".jpg" ,filetypes = [('JPG Files', '*.jpg*'),('PNG Files','*.png')])
	x=root.winfo_rootx()+canvas.winfo_x()
	y=root.winfo_rooty()+canvas.winfo_y()
	x1=x+canvas.winfo_width()
	y1=y+canvas.winfo_height()
	if file!=None:
	   ImageGrab.grab().crop((x,y,x1,y1)).save(file)
def openfile():
	file=askopenfilename(defaultextension=".jpg",filetypes=[('JPG Files',"*.jpg"),("PNG Files","*.png")])
	if file!=None:
		new()
		file=Image.open(file)
		canvas.image = ImageTk.PhotoImage(file)
		canvas.create_image(0, 0, image=canvas.image, anchor='nw')
def symetric(event):
	global symetric_drawing
	symetric_drawing=not(symetric_drawing)
def make_ellipse(event):
	canvas.create_oval(event.x-size/2,event.y-size/2,event.x+size/2,event.y+size/2,fill=color)
	if symetric_drawing:
		canvas.create_oval(root.winfo_width()-(event.x-size/2),event.y-size/2,root.winfo_width()-(event.x+size/2),event.y+size/2,fill=color)
def change_color(event,color_name):
	global color
	if color_name=="random":
		hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
		color=hexadecimal
	else:
	 	color=color_name
def change_size(event,size_number):
	global size
	if(workingEraser==False):
		size=size_number
	else:
		eraser_size=size_number
		print(eraser_size)
def eraser(event):
	global workingEraser
	workingEraser=True
def click(event):
	global prev
	prev=event
def move(event):
	global prev
	if(workingEraser==False):
		canvas.create_line(prev.x,prev.y,event.x,event.y,width=2,fill=color)
		if symetric_drawing:
			canvas.create_line(root.winfo_width()-prev.x,prev.y,root.winfo_width()-event.x,event.y,width=2,fill=color)
	else:
		canvas.create_oval(event.x-eraser_size/2,event.y-eraser_size/2,event.x+eraser_size/2,event.y+eraser_size/2,fill="white",outline="")
	prev=event
def new():
	canvas.delete('all')
def pointer(event):
	global workingEraser
	workingEraser=False
text_area=Text(root,bg="red",fg="white",width=15,font="arial 14 bold")
text_area.pack(side=LEFT,fill=Y)
canvas = Canvas(root,bg = "white",width=root.winfo_width()-15,height=root.winfo_height())
canvas.pack(fill=BOTH)
keys={"a":"random color","c":"circle","r":"red","b":"blue","y":"yellow","o":"orange","p":"pink","w":"brown","e":"eraser","l":"symetry","m":"pointer","sizes":"1,2,3"}
text=""
for key,value in keys.items():
	text+=key+" : "+value+"\n"
text_area.insert(1.0,text)
text_area.config(state=DISABLED)
root.bind('c',make_ellipse)
root.bind('b',lambda event:change_color(event,"blue"))
root.bind('g',lambda event:change_color(event,"green"))
root.bind('y',lambda event:change_color(event,"yellow"))
root.bind('r',lambda event:change_color(event,"red"))
root.bind('o',lambda event:change_color(event,"orange"))
root.bind('p',lambda event:change_color(event,"pink"))
root.bind('w',lambda event:change_color(event,"brown"))
root.bind('a',lambda event:change_color(event,"random"))
root.bind('1',lambda event:change_size(event,5))
root.bind('2',lambda event:change_size(event,10))
root.bind('3',lambda event:change_size(event,20))
root.bind('l',lambda event:symetric(event))
root.bind('e',lambda event:eraser(event))
root.bind('m',lambda event:pointer(event))
canvas.bind('<Button-1>',click)
canvas.bind('<B1-Motion>', move)
menu=Menu(root)
fileMenu=Menu(menu,tearoff=0)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_command(label="New",command=new)
fileMenu.add_command(label="Open",command=openfile)
menu.add_cascade(label="File",menu=fileMenu)
root.config(menu=menu)
def change_width():
	if(root.winfo_height()!=600):
		canvas.config(width=root.winfo_width(),height=root.winfo_height())
	root.after(500,change_width)
change_width()
root.mainloop()
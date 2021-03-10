from tkinter import * ## library that you need to use dor this to work
a = Tk()
a.geometry("400x400") ## window size
a.resizable(width=False, height=False)
a.configure(bg="pink", cursor="heart") ## here you can change some thing e.g. background color or cursor style
img = PhotoImage(file="flamingo.png") ## <-- here you need a flamingo image file named "flamingo.png"
canvas = Canvas(a, width = 400, height = 400, bg = "pink",bd=0, highlightthickness=0,)      
canvas.pack()
canvas.create_image(20,20,anchor=NW, image=img) 
a.title("flamingo") ## this changes the window title
a.iconphoto(False, img)
a.mainloop() ## you need this to have a window running

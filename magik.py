from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import webbrowser

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background='lightskyblue')

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root, text="File Name")
label_file_name.place(relx=0.25,rely=0.04,anchor=CENTER)

input_file_name = Entry(root, background='aliceblue')
input_file_name.place(relx=0.49,rely=0.04,anchor=CENTER)

my_text = Text(root,height=35,width=80,background='azure')
my_text.place(relx=0.51,rely=0.56,anchor=CENTER)

name = ""
file_path = ""
def openFile():
    global name
    global file_path
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    html_file = filedialog.askopenfilename(title="Open HTML File", filetypes=(("html files", "*.html"),))
    print(html_file)
    file_path=html_file
    name = os.path.basename(html_file)
    formated_name=name.split('.')[0]
    input_file_name.insert(END, formated_name)
    html_file = open(name,'r')
    paragraph=html_file.read()
    my_text.insert(END, paragraph)
    html_file.close()

def save():
    input_name = input_file_name.get()
    file = open(input_name+".html","w")
    data = my_text.get("1.0",END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
 
def run_html():
    global file_path
    webbrowser.open_new("file://" + file_path)

open_button=Button(root,image=open_img, command=openFile)
open_button.place(relx=0.06,rely=0.04,anchor=CENTER)

save_button=Button(root, image=save_img, text="Save File", command=save)
save_button.place(relx=0.11,rely=0.04,anchor=CENTER)

exit_button = Button(root,image=exit_img, text="Run File", command=run_html)
exit_button.place(relx=0.17,rely=0.04,anchor=CENTER)

root.mainloop()
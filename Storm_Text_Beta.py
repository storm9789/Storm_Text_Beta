# Storm Text Beta V.1
# Jacob Storm Reinsmith
import tkinter
from tkinter import *
from tkinter import messagebox


class scrollTxtArea:
    def __init__(self,root):
        frame=Frame(root)
        frame.pack()
        self.textPad(frame)

        
 
    def textPad(self,frame):
        #add a frame and put a text area into it
        textPad=Frame(frame)
        self.text=Text(textPad,height=50,width=90)
         
        # add a vertical scroll bar to the text area
        scroll=Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)
         
        #pack everything
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT,fill=Y)
        textPad.pack(side=TOP)

    def open_command():
        file = filedialog.askopenfile(mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            file.close()

def save_command():
    messagebox.showinfo("Error!", "This function is currently broken")

def exit_command():
    root.destroy()

def useless():
    messagebox.showinfo("Error!", "This function is currently broken")



def main():
    root = Tk()
    foo=scrollTxtArea(root)
    root.title('Storm Text Beta V.1')
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=main)
    filemenu.add_command(label="Open...", command=scrollTxtArea.open_command)
    filemenu.add_command(label="Save", command=save_command)
    filemenu.add_command(label="Save As", command=save_command)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit_command)
    helpmenu = Menu(menu)
    helpmenu.add_cascade(label="Help", menu=filemenu) # currently will not appear
    helpmenu.add_command(label="About...", command=useless)
    root.mainloop()
main()

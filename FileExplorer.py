import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os 

def browseFiles():
    filename = filedialog.askopenfilename(initialdir=os.path.expanduser("~/Desktop"),
                                          title="Select a File",
                                          filetypes=(("Text files", "*.txt*"),
                                                     ("all files", "*.*")))
      
    #se schimba din "File Explorer" in "File Opened"+ numele ferestrei deschise
    label_file_explorer.configure(text="File Opened: "+filename)
      
def browseFolders():
    foldername=filedialog.askdirectory(initialdir=os.path.expanduser("~/Desktop"),
                                       title="Select a Folder") 
    if foldername: 
       files=os.listdir(foldername) 
       if files:  
           file_list="\n".join(files) 
       else:
           file_list="Folderul este gol."
       label_file_explorer.configure(text="File Selected: "+foldername+"\n"+file_list)

#initializare fereastra
root=tk.Tk()
root.title("File Explorer")
root.geometry("700x400")
#setare background
root.config(background="white")

#creez butoanele "File Explorer,"Browse Files","Browse Folders","Exit"
label_file_explorer = Label(root, 
                            text = "File Explorer",
                            width = 100, height = 2, 
                            fg = "red")
  
      
button_explore = Button(root, 
                        text = "Browse Files",
                        command = browseFiles,fg="orange") 
button_folder = Button(root, 
                        text = "Browse Folders",
                        command = browseFolders,fg="blue") 
    
button_exit = Button(root, 
                     text = "Exit",
                     command = exit,fg="green") 
  
#plasez pe randuri si coloane ca intr-un tabel
label_file_explorer.grid(column = 1, row = 1) #sa fie puse pe mijloc
button_explore.grid(column = 1, row = 2)
button_folder.grid(column=1,row=3)  
button_exit.grid(column = 1,row = 4)

#pornire bucla principala
root.mainloop()







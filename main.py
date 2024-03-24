# tkinter is a library that allows for a very simple display
import tkinter as tk

# message box, and file dialog must be imported seperatly for use
from tkinter import messagebox, filedialog


import os
defaultSavePath = os.path.dirname(os.path.abspath(__file__)) + "\\notes"

# This function will clear the note, after warning the user
def clearNote():
    # Create an OK/Cancel message box, with the icon of warning, returns a true/false value
    responce = messagebox.askokcancel(title="WARNING", message="Are you sure you want to clear note?", icon='warning')
    # If the user selects ok...
    if responce:
        # Delete text for the first character, to the end of the text
        text.delete("1.0","end")
# This function will save the note as a new file
def saveAsNote():
    # Get all text for character 1, to the end of the text
    note = text.get("1.0", "end")
    # Create a windows save as dialog, with the default file extension of txt, limiting to only text files
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text  Files", "*.txt")], initialdir=defaultSavePath)
    # Set the current path lable's text as the path
    currentPath.config(text=path)
    # Run the save function with the path and the note
    save(path, note)

# This funciton will open a file
def importNote():
    # This will ask the user to open a file with the default file extension limited to the types of txt
    path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt")], initialdir=defaultSavePath)

    if path:
        with open(path, "r") as file:
           note = file.read()
           clearNote()

           text.insert("1.0", note) 
           currentPath.config(text=path)

def saveNote():
    path = currentPath.cget("text")
    if path:
        responce = messagebox.askokcancel("Save", "Saving will ovewrite the current file")
        if responce:
            note = text.get("1.0", "end")
            save(path, note)
    else:
        messagebox.showwarning("404", "Error 404: File not found; Creating new file")
        saveAsNote()


def save(path, note):
    if path:
        with open(path, "w") as file:
            file.write(note)
        messagebox.showinfo("Sucsess", "File was saved")
root = tk.Tk()
root.title("3/19/24 | PC")

text = tk.Text(root, wrap=tk.WORD)

text.pack(fill="both", expand=True)

clearbutton = tk.Button(root, text="Clear", command=clearNote)
clearbutton.pack(side=tk.LEFT)


openButton = tk.Button(root, text="Open", command=importNote)
openButton.pack(side="left")

currentPath = tk.Label(root)
currentPath.config(text="")
currentPath.pack(side="left")

submitButton = tk.Button(root, text="Save as", command=saveAsNote)
submitButton.pack(side="right")

saveButton = tk.Button(root, text="Save", command=saveNote)
saveButton.pack(side="right")

root.mainloop()
import tkinter as tk

from tkinter import messagebox, filedialog

def clearNote():
    responce = messagebox.askokcancel(title="WARNING", message="Are you sure you want to clear note?", icon='warning')
    if responce:
        text.delete("1.0","end")

def saveAsNote():
    note = text.get("1.0", "end")
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text  Filews", "*.txt")])
    currentPath.config(text=path)
    save(path, note)

def importNote():
    path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt")])

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
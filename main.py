import tkinter as tk

from tkinter import messagebox, filedialog

def clearNote():
    text.delete("1.0","end")

def saveAsNote():
    note = text.get("1.0", "end")
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text  Filews", "*.txt")])
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
    note = text.get("1.0", "end")
    save(path, note)


def save(path, note):
    if path:
        with open(path, "w") as file:
            file.write(note)
root = tk.Tk()
root.title("3/19/24 | PC")

text = tk.Text(root, wrap=tk.WORD)

text.pack(fill="both", expand=True)

clearbutton = tk.Button(root, text="clear note", command=clearNote)
clearbutton.pack(side=tk.LEFT)

currentPath = tk.Label(root)
currentPath.config(text="N/A")
currentPath.pack(side="left")
submitButton = tk.Button(root, text="Save as", command=saveAsNote)
submitButton.pack(side="right")

openButton = tk.Button(root, text="Open File", command=importNote)
openButton.pack(side="right")

saveButton = tk.Button(root, text="Save", command=saveNote)
saveButton.pack(side="right")
root.mainloop()
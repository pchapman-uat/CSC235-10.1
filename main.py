# tkinter is a library that allows for a very simple display
import tkinter as tk

# message box, and file dialog must be imported seperatly for use
from tkinter import messagebox, filedialog
# Import OS, it is used to get the current path for the python project
import os
# "os.path.abspath(__file__)" gets the path of the python file
# "os.path.dirname(...)" gets the directory of the python file
# + "\\notes" is added to the string to specify the folder for the notes
defaultSavePath = os.path.dirname(os.path.abspath(__file__)) + "\\notes"

# This function will clear the note, after warning the user
def clearNote():
    note = text.get("1.0", "end")
    length = len(note)
    if(length > 1):
        response = messagebox.askyesnocancel("Warning", "This action will remove unsaved work, do you want to save?")
        if(response):
            saveNote()
        elif (not (response == None)):
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

    # Clear the current viewed note
    # Clearing will ask the user if they want to save
    clearNote()
    # This will ask the user to open a file with the default file extension limited to the types of txt
    path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt")], initialdir=defaultSavePath)

    # If the path with the file exists...
    if path:
        # Open the file as read
        with open(path, "r") as file:
            # Read the file and save it to the note
            note = file.read()
            # Insert the note at line 1, character 0
            text.insert("1.0", note) 
            # Update the current path lable's text with the new path
            currentPath.config(text=path)

# Save the note with the current open file
def saveNote():
    # From the current path object get the text for the path
    path = currentPath.cget("text")
    # If there is a path...
    if path:
        # Ask the user for confirmation "ok" returns true "cancle" returns false
        responce = messagebox.askokcancel("Save", "Saving will ovewrite the current file")
        # IF the user selects "ok"
        if responce:
            # Get the text of the opened note, and save it to the note variable
            note = text.get("1.0", "end")
            # Run the save function with the path and note data
            save(path, note)
    # If there is no opened note...
    else:
        # Warn the user that we are saving as a new file
        messagebox.showwarning("404", "Error 404: File not found; Creating new file")
        # Run the save as note function
        saveAsNote()

# Save the note with the inputed path
def save(path, note):
    # If path exists...
    if path:
        # Open the file in write mode
        with open(path, "w") as file:
            # Write the file with the note text
            file.write(note)
        # Display that the note was saved sucsefully
        messagebox.showinfo("Sucsess", "File was saved")
# Create the root tk window
root = tk.Tk()
# Set the title of the window
root.title("3/19/24 | PC")

# Create a text object for the window, with the wrapping set to per word
text = tk.Text(root, wrap=tk.WORD)

# Pack, or show on screen, with a fill of both (horizontal, and vertical), with expanding set to true
text.pack(fill="both", expand=True)

# Create a button object for the window, with the text set to clear, with the command to the clearNote function
clearbutton = tk.Button(root, text="Clear", command=clearNote)
# Pack it to the left side of the window
clearbutton.pack(side="left")

# Create a button, same as the clear button, but with different text and command
openButton = tk.Button(root, text="Open", command=importNote)
# Pack it to the left side of the window
openButton.pack(side="left")

# Create a lable, this is text that is displayed, but not editable
currentPath = tk.Label(root)
# Set the current text to blank
# For lables you change the text in the config
currentPath.config(text="")
# Pack it to the left side of the window
currentPath.pack(side="left")

# Create a save as button, the same as the other buttons with different text and commands
submitButton = tk.Button(root, text="Save as", command=saveAsNote)
# Pack the button to the right side of the screen
submitButton.pack(side="right")

# Create a save button, same as others but with differnt text and command
saveButton = tk.Button(root, text="Save", command=saveNote)
# Pack the button to the right side
saveButton.pack(side="right")

# This will start the loop for the project
# Unlike pygame this will handle all of the events, including button presses, inputs, and closing the application
# When the user closes the application it will end loop, thus the python as well
root.mainloop()
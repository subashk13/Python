import tkinter as tk

root=tk.Tk()
root.title("FIRST GUI!")
root.geometry("500x600")

label=tk.Label(root,text="HELLO!",font=("Arial",15))
label.pack(pady=20)

def on_click():
    label.config(text="YOU CLICKED:)")

button=tk.Button(root,text="CLICK ME...",command=on_click)
button.pack()

root.mainloop()
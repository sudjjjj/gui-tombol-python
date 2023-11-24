import tkinter as tk

class SimpleGui:
    def __init__(self, root):
      self.root = root
      self.root.title("simple gui")
      self.label = tk.Label(root,text="hello,tk")
      self.label.pack()
      self.button = tk.Button(root, text="Click Me", command=self.change_text)
      self.button.pack()
      self.root.geometry("400x300")

    def change_text(self):
      self.label.config(text="Button clicked")

root = tk.Tk()
gui = SimpleGui(root)
root.mainloop()

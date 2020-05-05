import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)


if __name__ == "__main__":

    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Manage EC2")
    # TODO add icon root.iconbitmap https://www.youtube.com/watch?v=NoTM8JciWaQ
    root.geometry("650x450+200+200")
    root.resizable(False, False)

    # canvas = tk.Canvas(root, width=640, height=440, bg='#6872f4')
    # canvas.pack(side=tk.LEFT)

    lable1 = tk.Label(root, text="main ", justify='center')
    lable1.pack()


root.mainloop()
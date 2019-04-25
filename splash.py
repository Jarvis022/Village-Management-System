import Tkinter as tk
def splas():
    root = tk.Tk()
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))
    image_file = "ab.gif"
    image = tk.PhotoImage(file=image_file)
    canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="brown")
    canvas.create_image(width*0.8/2, height*0.8/2, image=image)
    canvas.pack()
    root.after(5000, root.destroy)
    root.mainloop()


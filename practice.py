import tkinter as tk


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

    root = tk.Tk()
    root.geometry("400x600")
    root.title("School Personnel Database")
    root.config(bg='DeepSkyBlue4')

    img = tk.PhotoImage(file="UniversityLogo.png")
    img = img.subsample(5, 4)  # subsample shrinks the image, in this case by 4x

    frame1 = tk.LabelFrame(root, padx=5, pady=5)
    frame1.config(bg='gold')
    frame1.grid(row=0, column=0, padx=10, pady=10)

    frame2 = tk.LabelFrame(root, padx=5, pady=5)
    frame2.config(bg='gold')
    frame2.grid(row=1, column=0, padx=10, pady=10)

    frame3 = tk.LabelFrame(root, padx=5, pady=5)
    frame3.config(bg='gold')
    frame3.grid(row=2, column=0, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

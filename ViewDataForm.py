import tkinter as tk


class ViewDataForm(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("App")
        self.background_color = "gray17"
        self.font_color = "grey83"
        self.iconbitmap("ico.ico")
        self.config(bg=self.background_color)
        self.geometry("1020x300")

        self.frame_lb = tk.Frame(background=self.background_color)
        self.frame_lb.pack(side=tk.RIGHT)
        self.listbox = tk.Listbox(self.frame_lb, height=720, listvariable=tk.Variable(
            value=("Test1", "Test2", "Test3")), font=50, background=self.background_color, fg=self.font_color, activestyle="none", relief="raised")
        self.listbox.pack(side=tk.LEFT)

        self.frame_data = tk.Frame(background=self.background_color)
        self.frame_data.pack(side=tk.TOP)

        self.search = tk.Entry(
            self.frame_lb, background=self.background_color, fg=self.font_color, bg=self.background_color)
        self.search.pack(side=tk.TOP)

        self.static_label_A = tk.Label(
            self.frame_data, text="Label A", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_A = tk.Label(
            self.frame_data, bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_A.grid(row=1, column=1)
        self.static_label_A.grid(row=1, column=0)
        self.static_label_B = tk.Label(
            self.frame_data, text="Label B", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_B = tk.Label(
            self.frame_data, bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_B.grid(row=2, column=1)
        self.static_label_B.grid(row=2, column=0)
        self.static_label_C = tk.Label(
            self.frame_data, text="Label C", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_C = tk.Label(
            self.frame_data, bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_C.grid(row=3, column=1)
        self.static_label_C.grid(row=3, column=0)
        self.static_label_D = tk.Label(
            self.frame_data, text="Label D", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_D = tk.Label(
            self.frame_data, bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_D.grid(row=4, column=1)
        self.static_label_D.grid(row=4, column=0)
        self.static_label_E = tk.Label(
            self.frame_data, text="Label E", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_E = tk.Label(
            self.frame_data, bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_E.grid(row=5, column=1)
        self.static_label_E.grid(row=5, column=0)
        self.static_label_F = tk.Label(
            self.frame_data, text="Label F", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_F = tk.Label(
            self.frame_data, bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_F.grid(row=6, column=1)
        self.static_label_F.grid(row=6, column=0)

        self.add_button = tk.Button(
            self.frame_data, text="ADD", bg=self.background_color, fg=self.font_color, font=100)
        self.add_button.grid(row=7, column=0)
        self.edit_button = tk.Button(
            self.frame_data, text="EDIT", bg=self.background_color, fg=self.font_color, font=100)
        self.edit_button.grid(row=7, column=1)
        self.delete_button = tk.Button(
            self.frame_data, text="DELETE", bg=self.background_color, fg=self.font_color, font=100)
        self.delete_button.grid(row=7, column=2)
        self.show_button = tk.Button(
            self.frame_data, text="SHOW", bg=self.background_color, fg=self.font_color, font=100)
        self.show_button.grid(row=7, column=3)


app = ViewDataForm()
app.mainloop()

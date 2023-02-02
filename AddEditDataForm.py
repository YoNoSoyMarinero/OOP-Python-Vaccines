from tkcalendar import DateEntry
import tkinter as tk
from Data import Data


class AddEditDataForm(tk.Toplevel):
    def __init__(self, master, data: Data) -> None:
        super(AddEditDataForm, self).__init__(master)

        self.title("App")
        self.background_color = "gray17"
        self.font_color = "grey83"
        self.iconbitmap("ico.ico")
        self.config(bg=self.background_color)
        self.geometry("350x375")
        self.data = data

        self.VarA = tk.StringVar(master)
        self.VarB = tk.StringVar(master)
        self.VarC = tk.StringVar(master)
        self.VarD = tk.StringVar(master)
        self.VarE = tk.StringVar(master)
        self.VarF = tk.StringVar(master)

        self.frame_data = tk.Frame(self, background=self.background_color)
        self.frame_data.pack()

        self.static_label_A = tk.Label(
            self.frame_data, text="Label A", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_A = tk.Entry(
            self.frame_data, bg=self.background_color, fg=self.font_color, font=100, textvariable=self.VarA)
        self.dynamic_label_A.grid(row=1, column=1, pady=5, sticky=tk.W)
        self.static_label_A.grid(row=1, column=0, pady=5, sticky=tk.E)
        self.static_label_B = tk.Label(
            self.frame_data, text="Label B", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_B = tk.Entry(
            self.frame_data, bg=self.background_color, fg=self.font_color, font=100, textvariable=self.VarB)
        self.dynamic_label_B.grid(row=2, column=1, pady=5, sticky=tk.W)
        self.static_label_B.grid(row=2, column=0, pady=5, sticky=tk.E)
        self.static_label_C = tk.Label(
            self.frame_data, text="Label C", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_C = tk.Entry(
            self.frame_data, bg=self.background_color, fg=self.font_color, font=100, textvariable=self.VarC)
        self.dynamic_label_C.grid(row=3, column=1, pady=5, sticky=tk.W)
        self.static_label_C.grid(row=3, column=0, pady=5, sticky=tk.E)
        self.static_label_D = tk.Label(
            self.frame_data, text="Label D", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_D = DateEntry(
            self.frame_data, width=16, bg=self.background_color, fg=self.font_color, bd=2, textvariable=self.VarD, date_pattern='yyyy/m/d')
        self.dynamic_label_D.grid(row=4, column=1, pady=5, sticky=tk.W)
        self.static_label_D.grid(row=4, column=0, pady=5, sticky=tk.E)
        self.static_label_E = tk.Label(
            self.frame_data, text="Label E", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_E = tk.Entry(
            self.frame_data, bg=self.background_color, fg=self.font_color, font=100, textvariable=self.VarE)
        self.dynamic_label_E.grid(row=5, column=1, pady=5, sticky=tk.W)
        self.static_label_E.grid(row=5, column=0, pady=5, sticky=tk.E)
        self.static_label_F = tk.Label(
            self.frame_data, text="Label F", bg=self.background_color, fg=self.font_color, font=100)
        self.dynamic_label_F = tk.Entry(
            self.frame_data, bg=self.background_color, fg=self.font_color, font=100, textvariable=self.VarF)
        self.dynamic_label_F.grid(row=6, column=1, pady=5, sticky=tk.W)
        self.static_label_F.grid(row=6, column=0, pady=5, sticky=tk.E)

        self.save_button = tk.Button(
            self.frame_data, bg=self.background_color, fg='lime green', text="SAVE", font=20)
        self.save_button.grid(row=7, column=0, pady=30)

        self.cancle_button = tk.Button(
            self.frame_data, bg=self.background_color, fg='IndianRed1', text="CANCLE", font=20)
        self.cancle_button.grid(row=7, column=1, pady=30, padx=5)

        self.transient(master)
        self.focus_force()
        self.grab_set()

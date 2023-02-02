import tkinter as tk
from Data import Data
from ViewCitizenForm import ViewCitizenForm


class MainForm(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.data = Data()
        self.data.load_data()
        self.title("App")
        self.background_color = "gray17"
        self.font_color = "grey83"
        self.geometry("400x400")
        self.iconbitmap("ico.ico")
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar, bg=self.background_color)
        self.exit_menu = tk.Menu(self.menubar, tearoff=False)
        self.exit_menu.add_command(label="Exit", command=self.destroy)

        self.data_menu = tk.Menu(self.menubar, tearoff=False)
        self.data_menu.add_command(
            label="Citizens", command=lambda: ViewCitizenForm(self, self.data))
        self.data_menu.add_command(label="Medical workers")
        self.data_menu.add_command(label="Digital certificates")
        self.data_menu.add_command(label="Vaccines")
        self.data_menu.add_command(label="Vaccinations certificates")
        self.data_menu.add_command(label="Doses")

        self.menubar.add_cascade(label="File", menu=self.exit_menu)
        self.menubar.add_cascade(label="Data", menu=self.data_menu)

        self.front_frame_label = tk.Label(
            self, text="Welcome!", background=self.background_color, fg=self.font_color, font=60)
        self.front_frame_label.pack(padx=30, pady=30)

        self.focus_force()


main = MainForm()
main.mainloop()

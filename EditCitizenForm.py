from AddEditDataForm import AddEditDataForm
import tkinter as tk
from tkinter import messagebox
from datetime import date


class EditCitizenForm(AddEditDataForm):

    def edit_citizen_command(self):
        name = self.VarA.get()
        surname = self.VarB.get()
        sex = self.VarF.get()

        try:
            self.data.edit_citizen(self.citizen.id, name,
                                   surname, sex)
            self.data.save_data()
            self.cancle = False
            self.destroy()
        except Exception as e:
            messagebox.showwarning("Warning!", e)

    def __init__(self, master, data, citizen) -> None:
        super().__init__(master, data)
        self.static_label_A['text'] = "Name: "
        self.static_label_B['text'] = "Surname: "
        self.static_label_C['text'] = "JMBG: "
        self.static_label_D['text'] = "Date of birth: "
        self.static_label_E['text'] = "ID:  "
        self.static_label_F['text'] = "Sex: "
        self.cancle_button['command'] = lambda: self.destroy()
        self.save_button['command'] = self.edit_citizen_command
        self.citizen = citizen
        self.VarA.set(self.citizen.name)
        self.VarB.set(self.citizen.surname)
        self.VarC.set(self.citizen.JMBG)
        self.VarD.set(self.citizen.date_of_birth)
        self.VarE.set(self.citizen.id)
        self.VarF.set(self.citizen.sex)

        self.dynamic_label_D['state'] = tk.DISABLED
        self.dynamic_label_C['state'] = tk.DISABLED
        self.dynamic_label_E['state'] = tk.DISABLED
        self.cancle = True

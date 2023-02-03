from AddEditDataForm import AddEditDataForm
from Vaccine import Vaccine
from datetime import date
import tkinter as tk
from tkinter import messagebox


class EditVaccineForm(AddEditDataForm):

    def edit_vaccine_command(self):
        name = self.VarA.get()
        serial_number = self.VarB.get()
        country = self.VarC.get()

        try:
            self.data.edit_vaccine(self.vaccine.id, name,
                                   country, serial_number)
            self.data.save_data()
            self.cancle = False
            self.destroy()
        except Exception as e:
            messagebox.showwarning("Warning!", e)

    def __init__(self, master, data, vaccine) -> None:
        super().__init__(master, data)

        self.static_label_A['text'] = "Name: "
        self.static_label_B['text'] = "Serial number: "
        self.static_label_C['text'] = "Country: "
        self.static_label_D['text'] = "Experation date: "
        self.static_label_E['text'] = ""
        self.static_label_F['text'] = ""
        self.cancle_button['command'] = lambda: self.destroy()
        self.save_button['command'] = self.edit_vaccine_command
        self.vaccine = vaccine

        self.VarA.set(self.vaccine.name)
        self.VarB.set(self.vaccine.serial_number)
        self.VarC.set(self.vaccine.country)
        self.VarD.set(self.vaccine.expire_date)

        self.dynamic_label_B['state'] = tk.DISABLED
        self.dynamic_label_D['state'] = tk.DISABLED
        self.dynamic_label_E.destroy()
        self.dynamic_label_F.destroy()
        self.cancle = True

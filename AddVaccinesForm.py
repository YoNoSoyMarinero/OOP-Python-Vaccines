from AddEditDataForm import AddEditDataForm
from Vaccine import Vaccine
from datetime import date
from tkinter import messagebox


class AddVaccineForm(AddEditDataForm):

    def command_add(self):
        name = self.VarA.get()
        serial_number = self.VarB.get()
        country = self.VarC.get()
        exp_date = self.VarD.get().split("/")
        exp_date = date(int(exp_date[0]), int(
            exp_date[1]), int(exp_date[2]))
        id = self.VarE.get()
        sex = self.VarF.get()
        try:
            vaccine = Vaccine(name, serial_number, country, exp_date)
            self.data.add_vaccine(vaccine)
            self.data.save_data()
            self.cancle = False
            self.destroy()
        except Exception as e:
            messagebox.showwarning("Warning", e)

    def __init__(self, master, data) -> None:
        super().__init__(master, data)

        self.static_label_A['text'] = "Name: "
        self.static_label_B['text'] = "Serial number: "
        self.static_label_C['text'] = "Country: "
        self.static_label_D['text'] = "Experation date: "
        self.static_label_E['text'] = ""
        self.static_label_F['text'] = ""

        self.dynamic_label_E.destroy()
        self.dynamic_label_F.destroy()
        self.save_button['command'] = self.command_add
        self.cancle_button['command'] = self.destroy
        self.cancle = True

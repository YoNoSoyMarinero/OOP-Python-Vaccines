from AddEditDataForm import AddEditDataForm
from Citizen import Citizen
from datetime import date
from tkinter import messagebox


class AddCitizenForm(AddEditDataForm):

    def command_add(self):
        name = self.VarA.get()
        surname = self.VarB.get()
        JMBG = self.VarC.get()
        date_of_birth = self.VarD.get().split("/")
        date_of_birth = date(int(date_of_birth[0]), int(
            date_of_birth[1]), int(date_of_birth[2]))
        id = self.VarE.get()
        sex = self.VarF.get()
        try:
            citizen = Citizen(JMBG, name, surname, date_of_birth, sex, id)
            self.data.add_citizen(citizen)
            self.data.save_data()
            self.cancle = False
            self.destroy()
        except Exception as e:
            messagebox.showwarning("Warning", e)

    def __init__(self, master, data) -> None:
        super().__init__(master, data)

        self.static_label_A['text'] = "Name: "
        self.static_label_B['text'] = "Surname: "
        self.static_label_C['text'] = "JMBG "
        self.static_label_D['text'] = "Date of birth: "
        self.static_label_E['text'] = "ID: "
        self.static_label_F['text'] = "Sex: "
        self.save_button['command'] = self.command_add
        self.cancle_button['command'] = self.destroy
        self.cancle = True

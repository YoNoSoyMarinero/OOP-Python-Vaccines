from AddEditDataForm import AddEditDataForm
from MedicalWorker import MedicalWorker
from datetime import date
from tkinter import messagebox


class AddMedicalWorkerForm(AddEditDataForm):

    def command_add(self):
        name = self.VarA.get()
        surname = self.VarB.get()
        JMBG = self.VarC.get()
        date_of_birth = self.VarD.get().split("/")
        date_of_birth = date(int(date_of_birth[0]), int(
            date_of_birth[1]), int(date_of_birth[2]))
        hospital = self.VarE.get()
        sex = self.VarF.get()
        try:
            medical_worker = MedicalWorker(
                JMBG, name, surname, date_of_birth, sex, hospital)
            self.data.add_medical_worker(medical_worker)
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
        self.static_label_E['text'] = "Hospital: "
        self.static_label_F['text'] = "Sex: "
        self.save_button['command'] = self.command_add
        self.cancle_button['command'] = self.destroy
        self.cancle = True

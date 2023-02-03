from AddEditDataForm import AddEditDataForm
import tkinter as tk
from tkinter import messagebox
from datetime import date


class EditMedicalWorkerForm(AddEditDataForm):

    def edit_medical_worker_command(self):
        name = self.VarA.get()
        surname = self.VarB.get()
        hospital = self.VarE.get()
        sex = self.VarF.get()

        try:
            self.data.edit_medical_worker(self.medical_worker.id, name,
                                          surname, hospital, sex)
            self.data.save_data()
            self.cancle = False
            self.destroy()
        except Exception as e:
            messagebox.showwarning("Warning!", e)

    def __init__(self, master, data, medical_worker) -> None:
        super().__init__(master, data)
        self.static_label_A['text'] = "Name: "
        self.static_label_B['text'] = "Surname: "
        self.static_label_C['text'] = "JMBG: "
        self.static_label_D['text'] = "Date of birth: "
        self.static_label_E['text'] = "Hospital:  "
        self.static_label_F['text'] = "Sex: "
        self.cancle_button['command'] = lambda: self.destroy()
        self.save_button['command'] = self.edit_medical_worker_command
        self.medical_worker = medical_worker
        self.VarA.set(self.medical_worker.name)
        self.VarB.set(self.medical_worker.surname)
        self.VarC.set(self.medical_worker.JMBG)
        self.VarD.set(self.medical_worker.date_of_birth)
        self.VarE.set(self.medical_worker.health_institution)
        self.VarF.set(self.medical_worker.sex)

        self.dynamic_label_D['state'] = tk.DISABLED
        self.dynamic_label_C['state'] = tk.DISABLED
        self.cancle = True

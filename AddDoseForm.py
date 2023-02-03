from AddEditDataForm import AddEditDataForm
from Dose import Dose
from datetime import date
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


class AddDoseForm(AddEditDataForm):

    def command_add(self):
        citizen = self.data.citizens[self.dynamic_label_A.current()]
        medical_worker = self.data.medical_workers[self.dynamic_label_B.current(
        )]
        vaccine = self.data.vaccines[self.dynamic_label_C.current()]
        dosage_date = self.VarD.get().split("/")
        dosage_date = date(int(dosage_date[0]), int(
            dosage_date[1]), int(dosage_date[2]))
        country = self.VarE.get()
        try:
            dose = Dose(dosage_date, vaccine, medical_worker, citizen, country)
            self.data.add_dose(dose)
            self.data.save_data()
            self.cancle = False
            self.destroy()
        except Exception as e:
            messagebox.showwarning("Warning", e)

    def __init__(self, master, data) -> None:
        super().__init__(master, data)

        self.static_label_A['text'] = "Citizen: "
        self.static_label_B['text'] = "Medical worker: "
        self.static_label_C['text'] = "Vaccine: "
        self.static_label_D['text'] = "Dosage date: "
        self.static_label_E['text'] = "Country: "
        self.static_label_F['text'] = ""

        self.dynamic_label_A.destroy()
        self.dynamic_label_A = ttk.Combobox(self.frame_data, width=30)
        self.dynamic_label_A.grid(row=1, column=1, pady=5)
        self.dynamic_label_A['values'] = tuple(
            citizen.name + " " + citizen.surname for citizen in self.data.citizens)

        self.dynamic_label_B.destroy()
        self.dynamic_label_B = ttk.Combobox(self.frame_data, width=30)
        self.dynamic_label_B.grid(row=2, column=1, pady=5)
        self.dynamic_label_B['values'] = tuple(
            medical_worker.name + " " + medical_worker.surname for medical_worker in self.data.medical_workers)

        self.dynamic_label_C.destroy()
        self.dynamic_label_C = ttk.Combobox(self.frame_data, width=30)
        self.dynamic_label_C.grid(row=3, column=1, pady=5)
        self.dynamic_label_C['values'] = tuple(
            vaccine.name for vaccine in self.data.vaccines)

        self.dynamic_label_F.destroy()
        self.save_button['command'] = self.command_add
        self.cancle_button['command'] = self.destroy
        self.cancle = True

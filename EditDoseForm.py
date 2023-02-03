from AddEditDataForm import AddEditDataForm
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class EditDoseForm(AddEditDataForm):

    def edit_dose_command(self):
        citizen = self.data.citizens[self.dynamic_label_A.current()]
        medical_worker = self.data.medical_workers[self.dynamic_label_B.current(
        )]
        vaccine = self.data.vaccines[self.dynamic_label_C.current()]
        country = self.VarE.get()

        try:
            self.data.edit_dose(self.dose.id, medical_worker,
                                citizen, vaccine, country)
            self.data.save_data()
            self.cancle = False
            self.destroy()
        except Exception as e:
            messagebox.showwarning("Warning!", e)

    def __init__(self, master, data, dose) -> None:
        super().__init__(master, data)

        self.static_label_A['text'] = "Citizen: "
        self.static_label_B['text'] = "Medical worker: "
        self.static_label_C['text'] = "Vaccine: "
        self.static_label_D['text'] = "Dosage date: "
        self.static_label_E['text'] = "Country: "
        self.static_label_F['text'] = ""
        self.cancle_button['command'] = lambda: self.destroy()
        self.save_button['command'] = self.edit_dose_command
        self.dose = dose

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

        self.VarD.set(self.dose.dosage_date)
        self.VarE.set(self.dose.country)
        self.dynamic_label_A.current(self.data.citizens.index(dose.citizen))
        self.dynamic_label_B.current(
            self.data.medical_workers.index(dose.medical_worker))
        self.dynamic_label_C.current(self.data.vaccines.index(dose.vaccine))

        self.dynamic_label_D['state'] = tk.DISABLED

        self.dynamic_label_F.destroy()
        self.cancle = True

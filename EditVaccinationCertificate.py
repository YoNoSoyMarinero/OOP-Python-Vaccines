from AddEditDataForm import AddEditDataForm
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class EditVaccinationCertificateForm(AddEditDataForm):

    def edit_vaccination_certificate_command(self):
        citizen = self.data.citizens[self.dynamic_label_A.current()]
        medical_worker = self.data.medical_workers[self.dynamic_label_B.current(
        )]
        dose = self.data.doses[self.dynamic_label_C.current()]
        certifcate_id = self.VarE.get()

        try:
            self.data.edit_vaccination_certificate(
                self.vaccination_certificate.id, medical_worker, citizen, dose, certifcate_id)
            self.data.save_data()
            self.cancle = False
            self.destroy()
        except Exception as e:
            messagebox.showwarning("Warning!", e)

    def __init__(self, master, data, vaccination_certificate) -> None:
        super().__init__(master, data)

        self.static_label_A['text'] = "Citizen: "
        self.static_label_B['text'] = "Medical worker: "
        self.static_label_C['text'] = "Dose: "
        self.static_label_D['text'] = "Date: "
        self.static_label_E['text'] = "Certification ID: "
        self.static_label_F['text'] = ""
        self.cancle_button['command'] = lambda: self.destroy()
        self.save_button['command'] = self.edit_vaccination_certificate_command
        self.vaccination_certificate = vaccination_certificate

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
            dose.dosage_date for dose in self.data.doses)

        self.VarD.set(self.vaccination_certificate.issuance_date)
        self.VarE.set(self.vaccination_certificate.certificate_id)
        self.dynamic_label_A.current(
            self.data.citizens.index(vaccination_certificate.citizen))
        self.dynamic_label_B.current(
            self.data.medical_workers.index(vaccination_certificate.medical_worker))
        self.dynamic_label_C.current(
            self.data.doses.index(vaccination_certificate.dose))

        self.dynamic_label_D['state'] = tk.DISABLED
        self.dynamic_label_E['state'] = tk.DISABLED

        self.dynamic_label_F.destroy()
        self.cancle = True

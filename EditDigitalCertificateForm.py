from AddEditDataForm import AddEditDataForm
from DigitacCertificate import DigitalCertificate
from datetime import date
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


class EditDigitalCertificateForm(AddEditDataForm):

    def edit_digital_certificate_command(self):
        citizen = self.data.citizens[self.dynamic_label_A.current()]
        certificate_id = self.VarB.get()

        try:
            self.data.edit_digital_certificate(
                self.digital_certificate.id, citizen, certificate_id)
            self.data.save_data()
            self.cancle = False
            self.destroy()
        except Exception as e:
            messagebox.showwarning("Warning!", e)

    def __init__(self, master, data, digital_certificate) -> None:
        super().__init__(master, data)

        self.static_label_A['text'] = "Citizen: "
        self.static_label_B['text'] = "Certification ID: "
        self.static_label_C['text'] = ""
        self.static_label_D['text'] = "Issuance date: "
        self.static_label_E['text'] = ""
        self.static_label_F['text'] = ""

        self.dynamic_label_A.destroy()
        self.digital_certificate = digital_certificate
        self.dynamic_label_A = ttk.Combobox(self.frame_data, width=30)
        self.dynamic_label_A.grid(row=1, column=1, pady=5)
        self.dynamic_label_A['values'] = tuple(
            citizen.name + " " + citizen.surname for citizen in self.data.citizens)

        self.dynamic_label_C.destroy()
        self.dynamic_label_E.destroy()
        self.dynamic_label_F.destroy()
        self.dynamic_label_D['state'] = tk.DISABLED
        self.dynamic_label_A.current(
            self.data.citizens.index(digital_certificate.citizen))
        self.VarB.set(digital_certificate.certificate_id)
        self.VarD.set(digital_certificate.issuance_date)

        self.save_button['command'] = self.edit_digital_certificate_command
        self.cancle_button['command'] = self.destroy
        self.cancle = True

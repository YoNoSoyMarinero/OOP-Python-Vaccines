from AddEditDataForm import AddEditDataForm
from DigitacCertificate import DigitalCertificate
from datetime import date
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


class AddDigitalCertificateForm(AddEditDataForm):

    def command_add(self):
        citizen = self.data.citizens[self.dynamic_label_A.current()]
        certification_id = self.VarB.get()
        dosage_date = self.VarD.get().split("/")
        dosage_date = date(int(dosage_date[0]), int(
            dosage_date[1]), int(dosage_date[2]))
        try:
            digital_certificate = DigitalCertificate(
                certification_id, dosage_date, citizen)
            self.data.add_digital_certificate(digital_certificate)
            self.data.save_data()
            self.cancle = False
            self.destroy()
        except Exception as e:
            messagebox.showwarning("Warning", e)

    def __init__(self, master, data) -> None:
        super().__init__(master, data)

        self.static_label_A['text'] = "Citizen: "
        self.static_label_B['text'] = "Certification ID: "
        self.static_label_C['text'] = ""
        self.static_label_D['text'] = "Issuance date: "
        self.static_label_E['text'] = ""
        self.static_label_F['text'] = ""

        self.dynamic_label_A.destroy()
        self.dynamic_label_A = ttk.Combobox(self.frame_data, width=30)
        self.dynamic_label_A.grid(row=1, column=1, pady=5)
        self.dynamic_label_A['values'] = tuple(
            citizen.name + " " + citizen.surname for citizen in self.data.citizens)

        self.dynamic_label_C.destroy()
        self.dynamic_label_E.destroy()
        self.dynamic_label_F.destroy()

        self.save_button['command'] = self.command_add
        self.cancle_button['command'] = self.destroy

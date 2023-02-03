from ViewDataForm import ViewDataForm
from AddVaccinationCertificateForm import AddVaccinationCertificateForm
from EditVaccinationCertificate import EditVaccinationCertificateForm
from tkinter import messagebox
import tkinter as tk


class ViewVaccinationCertificateForm(ViewDataForm):

    def queried_vaccination_certificates(self):
        query = self.query.get()
        if query == "":
            return self.data.vaccination_certificates
        else:
            return self.data.select_vaccination_certificates(query)

    def fill_listbox(self, event=None):
        self.clear()
        self.listbox.delete(0, tk.END)
        for vaccination_certificate in self.queried_vaccination_certificates():
            self.listbox.insert(tk.END, vaccination_certificate.certificate_id)

    def fill_labels(self, vaccination_certificate):
        self.dynamic_label_A['text'] = vaccination_certificate.citizen.name + \
            " " + vaccination_certificate.citizen.surname
        self.dynamic_label_B['text'] = vaccination_certificate.medical_worker.name + \
            " " + vaccination_certificate.medical_worker.surname
        self.dynamic_label_C['text'] = vaccination_certificate.issuance_date
        self.dynamic_label_D['text'] = vaccination_certificate.dose.vaccine.name
        self.dynamic_label_E['text'] = vaccination_certificate.certificate_id
        self.dynamic_label_F['text'] = ""

    def clear_labels(self):
        self.dynamic_label_A['text'] = ""
        self.dynamic_label_B['text'] = ""
        self.dynamic_label_C['text'] = ""
        self.dynamic_label_D['text'] = ""
        self.dynamic_label_E['text'] = ""
        self.dynamic_label_F['text'] = ""

    def clear(self):
        self.clear_labels()
        self.listbox.selection_clear(0, tk.END)

    def listbox_change(self, event=None):
        if not self.listbox.curselection():

            self.edit_button['state'] = tk.DISABLED
            self.delete_button['state'] = tk.DISABLED
            return

        index = self.listbox.curselection()[0]
        self.data.sort_data()
        vaccination_certificate = self.queried_vaccination_certificates()[
            index]
        self.fill_labels(vaccination_certificate)
        self.edit_button["state"] = tk.NORMAL
        self.delete_button["state"] = tk.NORMAL

    def add_vaccination_certificate_command(self):
        form = AddVaccinationCertificateForm(self, self.data)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        vaccination_certificate = self.data.vaccination_certificates[-1]
        self.data.sort_data()
        self.fill_listbox()
        self.listbox.select_set(
            self.data.vaccination_certificates.index(vaccination_certificate))
        self.listbox_change()

    def edit_vaccination_certificate_command(self):
        try:
            index = self.listbox.curselection()[0]
        except:
            messagebox.showwarning(
                "Warning!", "You have to select Vaccination certificate you want to edit!")
            return
        self.data.sort_data()
        vaccination_certificate = self.queried_vaccination_certificates()[
            index]
        form = EditVaccinationCertificateForm(
            self, self.data, vaccination_certificate)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        self.clear()
        self.fill_listbox()
        self.listbox.selection_set(index)
        self.listbox_change()

    def delete_vaccination_certificate_command(self):
        index = self.listbox.curselection()[0]
        self.data.sort_data()
        vaccination_certificate = self.queried_vaccination_certificates()[
            index]
        self.data.delete_vaccination_certificate(vaccination_certificate.id)
        self.fill_listbox()
        self.data.save_data()
        self.clear()

    def __init__(self, master, data) -> None:
        super().__init__(master, data)

        self.clear_button['command'] = self.clear
        self.edit_button['command'] = self.edit_vaccination_certificate_command
        self.add_button['command'] = self.add_vaccination_certificate_command
        self.delete_button['command'] = self.delete_vaccination_certificate_command
        self.static_label_A['text'] = "Citizen: "
        self.static_label_B['text'] = "Medical worker: "
        self.static_label_C['text'] = "Vaccination date: "
        self.static_label_D['text'] = "Vaccine: "
        self.static_label_E['text'] = "Certificate ID:  "
        self.static_label_F['text'] = ""

        self.show_button.destroy()

        self.listbox.bind("<<ListboxSelect>>", self.listbox_change)
        self.search.bind('<KeyRelease>', self.fill_listbox)

        self.fill_listbox()

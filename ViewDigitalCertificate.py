from ViewDataForm import ViewDataForm
from tkinter import messagebox
from AddDigitalCertificateForm import AddDigitalCertificateForm
from EditDigitalCertificateForm import EditDigitalCertificateForm
import tkinter as tk


class ViewDigitalCertifiacteForm(ViewDataForm):

    def queried_digital_certificates(self):
        query = self.query.get()
        if query == "":
            return self.data.digital_certificates
        else:
            return self.data.select_digital_certificates(query)

    def fill_listbox(self, event=None):
        self.clear()
        self.listbox.delete(0, tk.END)
        for digital_certificate in self.queried_digital_certificates():
            self.listbox.insert(tk.END, digital_certificate.certificate_id)

    def fill_labels(self, digital_certificate):
        self.dynamic_label_A['text'] = digital_certificate.citizen.name + \
            " " + digital_certificate.citizen.surname
        self.dynamic_label_B['text'] = digital_certificate.certificate_id
        self.dynamic_label_C['text'] = digital_certificate.issuance_date

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
        digital_certificate = self.queried_digital_certificates()[index]
        self.fill_labels(digital_certificate)
        self.edit_button["state"] = tk.NORMAL
        self.delete_button["state"] = tk.NORMAL

    def delete_digital_certificate_command(self):
        index = self.listbox.curselection()[0]
        self.data.sort_data()
        digital_certificate = self.queried_digital_certificates()[index]
        self.data.delete_digital_certificate(digital_certificate.id)
        self.fill_listbox()
        self.data.save_data()
        self.clear()

    def add_digital_certificate_command(self):
        form = AddDigitalCertificateForm(self, self.data)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        digital_certificate = self.data.digital_certificates[-1]
        self.data.sort_data()
        self.fill_listbox()
        self.listbox.select_set(
            self.data.digital_certificates.index(digital_certificate))
        self.listbox_change()

    def edit_digital_certificate_command(self):
        try:
            index = self.listbox.curselection()[0]
        except:
            messagebox.showwarning(
                "Warning!", "You have to select digital certificate you want to edit!")
            return
        self.data.sort_data()
        digital_certificate = self.queried_digital_certificates()[index]
        form = EditDigitalCertificateForm(self, self.data, digital_certificate)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        self.clear()
        self.fill_listbox()
        self.listbox.selection_set(index)
        self.listbox_change()

    def __init__(self, master, data, by_citizen=None) -> None:
        super().__init__(master, data)

        self.clear_button['command'] = self.clear
        self.edit_button['command'] = self.edit_digital_certificate_command
        self.add_button['command'] = self.add_digital_certificate_command
        self.delete_button['command'] = self.delete_digital_certificate_command
        self.static_label_A['text'] = "Citizen: "
        self.static_label_B['text'] = "Certificate id: "
        self.static_label_C['text'] = "Issuance date: "
        self.static_label_D['text'] = ""
        self.static_label_E['text'] = ""
        self.static_label_F['text'] = ""

        self.show_button.destroy()

        self.listbox.bind("<<ListboxSelect>>", self.listbox_change)
        self.search.bind('<KeyRelease>', self.fill_listbox)

        if (by_citizen):
            self.query.set(by_citizen)

        self.fill_listbox()

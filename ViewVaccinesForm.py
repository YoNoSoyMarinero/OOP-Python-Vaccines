from ViewDataForm import ViewDataForm
from AddVaccinesForm import AddVaccineForm
from EditVaccinesForm import EditVaccineForm
from tkinter import messagebox
import tkinter as tk


class ViewVaccinesForm(ViewDataForm):

    def queried_vaccines(self):
        query = self.query.get()
        if query == "":
            return self.data.vaccines
        else:
            return self.data.select_vaccines(query)

    def fill_listbox(self, event=None):
        self.clear()
        self.listbox.delete(0, tk.END)
        for vaccine in self.queried_vaccines():
            self.listbox.insert(tk.END, vaccine.name)

    def fill_labels(self, vaccine):
        self.dynamic_label_A['text'] = vaccine.name
        self.dynamic_label_B['text'] = vaccine.serial_number
        self.dynamic_label_C['text'] = vaccine.expire_date
        self.dynamic_label_D['text'] = vaccine.country

    def clear_labels(self):
        self.dynamic_label_A['text'] = ""
        self.dynamic_label_B['text'] = ""
        self.dynamic_label_C['text'] = ""
        self.dynamic_label_D['text'] = ""
        self.dynamic_label_E['text'] = ""
        self.dynamic_label_F['text'] = ""

    def clear(self, disable=False):
        self.clear_labels()
        self.listbox.selection_clear(0, tk.END)
        if disable:
            self.edit_button['state'] = tk.DISABLED
            self.delete_button['state'] = tk.DISABLED

    def listbox_change(self, event=None):
        if not self.listbox.curselection():

            self.edit_button['state'] = tk.DISABLED
            self.delete_button['state'] = tk.DISABLED
            return

        index = self.listbox.curselection()[0]
        self.data.sort_data()
        vaccines = self.queried_vaccines()[index]
        self.fill_labels(vaccines)
        self.edit_button["state"] = tk.NORMAL
        self.delete_button["state"] = tk.NORMAL

    def add_vaccine_command(self):
        form = AddVaccineForm(self, self.data)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        vaccine = self.data.vaccines[-1]
        self.data.sort_data()
        self.fill_listbox()
        self.listbox.select_set(self.data.vaccines.index(vaccine))
        self.listbox_change()

    def delete_vaccine_command(self):
        index = self.listbox.curselection()[0]
        self.data.sort_data()
        vaccine = self.queried_vaccines()[index]
        self.data.delete_vaccine(vaccine.id)
        self.fill_listbox()
        self.data.save_data()
        self.clear()

    def edit_vaccine_command(self):
        try:
            index = self.listbox.curselection()[0]
        except:
            messagebox.showwarning(
                "Warning!", "You have to select vaccine you want to edit!")
            return
        self.data.sort_data()
        vaccine = self.queried_vaccines()[index]
        form = EditVaccineForm(self, self.data, vaccine)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        self.clear(True)
        self.fill_listbox()
        self.listbox.selection_set(index)
        self.listbox_change()

    def __init__(self, master, data) -> None:
        super().__init__(master, data)

        self.clear_button['command'] = lambda: self.clear(True)
        self.edit_button['command'] = self.edit_vaccine_command
        self.add_button['command'] = self.add_vaccine_command
        self.delete_button['command'] = self.delete_vaccine_command
        self.static_label_A['text'] = "Name: "
        self.static_label_B['text'] = "Serial number: "
        self.static_label_C['text'] = "Expiration date: "
        self.static_label_D['text'] = "Country: "
        self.static_label_E['text'] = ""
        self.static_label_F['text'] = ""
        self.show_button.destroy()
        self.listbox.bind("<<ListboxSelect>>", self.listbox_change)
        self.search.bind('<KeyRelease>', self.fill_listbox)

        self.fill_listbox()

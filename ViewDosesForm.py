from ViewDataForm import ViewDataForm
from tkinter import messagebox
from AddDoseForm import AddDoseForm
from EditDoseForm import EditDoseForm
import tkinter as tk


class ViewDosesForm(ViewDataForm):

    def queried_doses(self):
        query = self.query.get()
        if query == "":
            return self.data.doses
        else:
            return self.data.select_dose(query)

    def fill_listbox(self, event=None):
        self.clear()
        self.listbox.delete(0, tk.END)
        for dose in self.queried_doses():
            self.listbox.insert(tk.END, dose.dosage_date)

    def fill_labels(self, dose):
        self.dynamic_label_A['text'] = dose.citizen.name + \
            " " + dose.citizen.surname
        self.dynamic_label_B['text'] = dose.medical_worker.name + \
            " " + dose.medical_worker.surname
        self.dynamic_label_C['text'] = dose.dosage_date
        self.dynamic_label_D['text'] = dose.vaccine.name
        self.dynamic_label_E['text'] = dose.country
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
        dose = self.queried_doses()[index]
        self.fill_labels(dose)
        self.edit_button["state"] = tk.NORMAL
        self.delete_button["state"] = tk.NORMAL

    def add_dose_command(self):
        form = AddDoseForm(self, self.data)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        dose = self.data.doses[-1]
        self.data.sort_data()
        self.fill_listbox()
        self.listbox.select_set(self.data.doses.index(dose))
        self.listbox_change()

    def delete_dose_command(self):
        index = self.listbox.curselection()[0]
        self.data.sort_data()
        dose = self.queried_doses()[index]
        self.data.delete_dose(dose.id)
        self.fill_listbox()
        self.data.save_data()
        self.clear()

    def edit_dose_command(self):
        try:
            index = self.listbox.curselection()[0]
        except:
            messagebox.showwarning(
                "Warning!", "You have to select dose you want to edit!")
            return
        self.data.sort_data()
        dose = self.queried_doses()[index]
        form = EditDoseForm(self, self.data, dose)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        self.clear()
        self.fill_listbox()
        self.listbox.selection_set(index)
        self.listbox_change()

    def __init__(self, master, data) -> None:
        super().__init__(master, data)

        self.add_button['command'] = self.add_dose_command
        self.clear_button['command'] = self.clear
        self.edit_button['command'] = self.edit_dose_command
        self.delete_button['command'] = self.delete_dose_command
        self.static_label_A['text'] = "Citizen: "
        self.static_label_B['text'] = "Medical worker: "
        self.static_label_C['text'] = "Dosage date: "
        self.static_label_D['text'] = "Vaccine: "
        self.static_label_E['text'] = "Country:  "
        self.static_label_F['text'] = ""

        self.show_button.destroy()

        self.listbox.bind("<<ListboxSelect>>", self.listbox_change)
        self.search.bind('<KeyRelease>', self.fill_listbox)

        self.fill_listbox()

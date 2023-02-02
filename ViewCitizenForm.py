from ViewDataForm import ViewDataForm
from AddCitizenForm import AddCitizenForm
from EditCitizenForm import EditCitizenForm
from Data import Data
from Citizen import Citizen
from datetime import datetime
from tkinter import messagebox
import tkinter as tk


class ViewCitizenForm(ViewDataForm):

    def queried_citizens(self):
        query = self.query.get()
        if query == "":
            return self.data.citizens
        else:
            return self.data.select_citizens(query)

    def fill_listbox(self, event=None):
        self.clear()
        self.listbox.delete(0, tk.END)
        for citizen in self.queried_citizens():
            self.listbox.insert(tk.END, citizen.name + " " + citizen.surname)

    def fill_labels(self, citizen):
        self.dynamic_label_A['text'] = citizen.name
        self.dynamic_label_B['text'] = citizen.surname
        self.dynamic_label_C['text'] = citizen.date_of_birth
        self.dynamic_label_D['text'] = citizen.JMBG
        self.dynamic_label_E['text'] = citizen.id
        self.dynamic_label_F['text'] = citizen.sex

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
        citizen = self.queried_citizens()[index]
        self.fill_labels(citizen)
        self.edit_button["state"] = tk.NORMAL
        self.delete_button["state"] = tk.NORMAL

    def add_citizen_command(self):
        form = AddCitizenForm(self, self.data)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        citizen = self.data.citizens[-1]
        self.data.sort_data()
        self.fill_listbox()
        self.listbox.select_set(self.data.citizens.index(citizen))
        self.listbox_change()

    def edit_citizen_command(self):
        try:
            index = self.listbox.curselection()[0]
        except:
            messagebox.showwarning(
                "Warning!", "You have to select citizen you want to edit!")
            return
        self.data.sort_data()
        citizen = self.queried_citizens()[index]
        form = EditCitizenForm(self, self.data, citizen)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        self.clear()
        self.fill_listbox()
        self.listbox.selection_set(index)
        self.listbox_change()

    def delete_citizen_command(self):
        index = self.listbox.curselection()[0]
        self.data.sort_data()
        citizen = self.queried_citizens()[index]
        self.data.delete_citizen(citizen.id)
        self.fill_listbox()
        self.data.save_data()
        self.clear()

    def __init__(self, master, data) -> None:
        super().__init__(master, data)

        self.add_button['command'] = self.add_citizen_command
        self.edit_button['command'] = lambda: EditCitizenForm(self, self.data)
        self.clear_button['command'] = self.clear
        self.delete_button['command'] = self.delete_citizen_command
        self.edit_button['command'] = self.edit_citizen_command
        self.static_label_A['text'] = "Name: "
        self.static_label_B['text'] = "Surname: "
        self.static_label_C['text'] = "Date of birth: "
        self.static_label_D['text'] = "JMBG: "
        self.static_label_E['text'] = "ID:  "
        self.static_label_F['text'] = "Sex: "

        self.listbox.bind("<<ListboxSelect>>", self.listbox_change)
        self.search.bind('<KeyRelease>', self.fill_listbox)

        self.fill_listbox()

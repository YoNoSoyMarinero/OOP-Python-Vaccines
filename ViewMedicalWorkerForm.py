from ViewDataForm import ViewDataForm
from AddMedicalWorkerForm import AddMedicalWorkerForm
from EditMedicalWorkerForm import EditMedicalWorkerForm
from Data import Data
from tkinter import messagebox
import tkinter as tk


class ViewMedicalWorkerForm(ViewDataForm):

    def listbox_change(self, event=None):
        if not self.listbox.curselection():

            self.edit_button['state'] = tk.DISABLED
            self.delete_button['state'] = tk.DISABLED
            return

        index = self.listbox.curselection()[0]
        self.data.sort_data()
        medical_worker = self.queried_medical_workers()[index]
        self.fill_labels(medical_worker)
        self.edit_button["state"] = tk.NORMAL
        self.delete_button["state"] = tk.NORMAL

    def clear_labels(self):
        self.dynamic_label_A['text'] = ""
        self.dynamic_label_B['text'] = ""
        self.dynamic_label_C['text'] = ""
        self.dynamic_label_D['text'] = ""
        self.dynamic_label_E['text'] = ""
        self.dynamic_label_F['text'] = ""

    def fill_labels(self, medical_worker):
        self.dynamic_label_A['text'] = medical_worker.name
        self.dynamic_label_B['text'] = medical_worker.surname
        self.dynamic_label_C['text'] = medical_worker.date_of_birth
        self.dynamic_label_D['text'] = medical_worker.JMBG
        self.dynamic_label_E['text'] = medical_worker.id
        self.dynamic_label_F['text'] = medical_worker.sex

    def queried_medical_workers(self):
        query = self.query.get()
        if query == "":
            return self.data.medical_workers
        else:
            return self.data.select_medical_workers(query)

    def fill_listbox(self, event=None):
        self.clear()
        self.listbox.delete(0, tk.END)
        for medical_worker in self.queried_medical_workers():
            self.listbox.insert(tk.END, medical_worker.name +
                                " " + medical_worker.surname)

    def clear(self):
        self.clear_labels()
        self.listbox.selection_clear(0, tk.END)

    def add_medical_worker_command(self):
        form = AddMedicalWorkerForm(self, self.data)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        medical_worker = self.data.medical_workers[-1]
        self.data.sort_data()
        self.fill_listbox()
        self.listbox.select_set(
            self.data.medical_workers.index(medical_worker))
        self.listbox_change()

    def edit_medical_worker_command(self):
        try:
            index = self.listbox.curselection()[0]
        except:
            messagebox.showwarning(
                "Warning!", "You have to select citizen you want to edit!")
            return
        self.data.sort_data()
        medical_worker = self.queried_medical_workers()[index]
        form = EditMedicalWorkerForm(self, self.data, medical_worker)
        self.clear()
        self.query.set("")
        form.wait_window()

        if form.cancle:
            return

        self.clear()
        self.fill_listbox()
        self.listbox.selection_set(index)
        self.listbox_change()

    def delete_medical_worker_command(self):
        index = self.listbox.curselection()[0]
        self.data.sort_data()
        medical_worker = self.queried_medical_workers()[index]
        self.data.delete_medical_worker(medical_worker.id)
        self.fill_listbox()
        self.data.save_data()
        self.clear()

    def __init__(self, master, data: Data) -> None:
        super().__init__(master, data)

        self.clear_button['command'] = self.clear
        self.delete_button['command'] = self.delete_medical_worker_command
        self.add_button['command'] = self.add_medical_worker_command
        self.edit_button['command'] = self.edit_medical_worker_command
        self.static_label_A['text'] = "Name: "
        self.static_label_B['text'] = "Surname: "
        self.static_label_C['text'] = "Date of birth: "
        self.static_label_D['text'] = "JMBG: "
        self.static_label_E['text'] = "Hospital:  "
        self.static_label_F['text'] = "Sex: "

        self.show_button.destroy()

        self.listbox.bind("<<ListboxSelect>>", self.listbox_change)
        self.search.bind('<KeyRelease>', self.fill_listbox)

        self.fill_listbox()

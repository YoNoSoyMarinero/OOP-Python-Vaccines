import pickle
from Citizen import Citizen
from DigitacCertificate import DigitalCertificate
from datetime import date


class Data:

    def find_index_for_deletion(self, list, id):
        for index in range(len(list)):
            if (list[index].id == id):
                return index

    def check_if_JMBG_not_unique(self, JMBG):
        return JMBG in [citizen.JMBG for citizen in self.citizens]

    def check_if_ID_not_unique(self, id_number):
        return id_number in [citizen.id_number for citizen in self.citizens]

    def check_if_serial_number_not_unique(self, serial_number):
        return serial_number in [vaccine.serial_number for vaccine in self.vaccines]

    def check_if_vaccination_certificate_id_not_unique(self, certificate_id):
        return certificate_id in [vaccination_certificate.certificate_id for vaccination_certificate in self.vaccination_certificates]

    def check_if_digital_certificate_not_unique(self, certificate_id):
        return certificate_id in [digital_certificate for digital_certificate in self.digital_certificates]

    def select_citizens(self, query):
        return list(filter(lambda citizen: query.upper() in citizen.surname.upper() + " " + citizen.name.upper(), self.citizens))

    def add_citizen(self, citizen):
        citizen.id = self.global_id
        self.global_id += 1
        self.citizens.append(citizen)

    def delete_citizen(self, id):
        citizen_to_delete = self.citizens[self.find_index_for_deletion(
            self.citizens, id)]

        if citizen_to_delete.digital_certificate:
            self.delete_digital_certificate(
                citizen_to_delete.digital_certificate.id)
        for dose in citizen_to_delete.doses_received:
            self.delete_dose(dose.id)
        for vaccination_certificate in citizen_to_delete.vaccination_certificates:
            self.delete_vaccination_certificate(vaccination_certificate.id)

        self.citizens.pop(self.find_index_for_deletion(self.citizens, id))

    def edit_citizen(self, id, name, surname, sex):
        self.citizens[self.find_index_for_deletion(
            self.citizens, id)].name = name
        self.citizens[self.find_index_for_deletion(
            self.citizens, id)].surname = surname
        self.citizens[self.find_index_for_deletion(
            self.citizens, id)].sex = sex

    def select_medical_workers(self, query):
        return list(filter(lambda medical_worker: query.upper() in medical_worker.surname.upper() + " " + medical_worker.name.upper(), self.medical_workers))

    def add_medical_worker(self, medical_worker):
        medical_worker.id = self.global_id
        self.global_id += 1
        self.medical_workers.append(medical_worker)

    def delete_medical_worker(self, id):
        self.medical_workers.pop(
            self.find_index_for_deletion(self.medical_workers, id))

    def edit_medical_worker(self, id, name, surname, health_institution, sex):
        self.medical_workers[self.find_index_for_deletion(
            self.medical_workers, id)].name = name
        self.medical_workers[self.find_index_for_deletion(
            self.medical_workers, id)].surname = surname
        self.medical_workers[self.find_index_for_deletion(
            self.medical_workers, id)].sex = sex
        self.medical_workers[self.find_index_for_deletion(
            self.medical_workers, id)].health_institution = health_institution

    def select_vaccines(self, query):
        return list(filter(lambda vaccine: query.upper() in vaccine.name.upper(), self.vaccines))

    def add_vaccine(self, vaccine):
        vaccine.id = self.global_id
        self.global_id += 1
        self.vaccines.append(vaccine)

    def delete_vaccine(self, id):
        self.vaccines.pop(self.find_index_for_deletion(self.vaccines, id))

    def edit_vaccine(self, id, name, country, serial_number):
        self.vaccines[self.find_index_for_deletion(
            self.vaccines, id)].name = name
        self.vaccines[self.find_index_for_deletion(
            self.vaccines, id)].country = country
        self.vaccines[self.find_index_for_deletion(
            self.vaccines, id)].serial_number = serial_number

    def select_dose(self, query):
        return list(filter(lambda dose: query.upper() in dose.citizen.surname.upper() + " " + dose.citizen.name.upper() + " " + dose.vaccine.name.upper(), self.doses))

    def add_dose(self, dose):
        dose.id = self.global_id
        self.global_id += 1
        self.doses.append(dose)

    def delete_dose(self, id):
        self.doses.pop(self.find_index_for_deletion(self.doses, id))

    def edit_dose(self, id, medical_worker, citizen, vaccine, country):
        self.doses[self.find_index_for_deletion(
            self.doses, id)].medical_worker = medical_worker
        self.doses[self.find_index_for_deletion(
            self.doses, id)].citizen = citizen
        self.doses[self.find_index_for_deletion(
            self.doses, id)].vaccine = vaccine
        self.doses[self.find_index_for_deletion(
            self.doses, id)].country = country

    def select_vaccination_certificates(self, query):
        return list(filter(lambda vaccination_certificate: query.upper() in vaccination_certificate.citizen.name.upper() + " " + vaccination_certificate.citizen.surname.upper(), self.vaccination_certificates))

    def add_vaccination_certificate(self, vaccination_certificate):
        vaccination_certificate.id = self.global_id
        self.global_id += 1
        self.vaccination_certificates.append(vaccination_certificate)

    def delete_vaccination_certificate(self, id):
        self.vaccination_certificates.pop(
            self.find_index_for_deletion(self.vaccination_certificates, id))

    def edit_vaccination_certificate(self, id, medical_worker, citizen, dose, certificate_id):
        self.vaccination_certificates[self.find_index_for_deletion(
            self.vaccination_certificates, id)].medical_worker = medical_worker
        self.vaccination_certificates[self.find_index_for_deletion(
            self.vaccination_certificates, id)].citizen = citizen
        self.vaccination_certificates[self.find_index_for_deletion(
            self.vaccination_certificates, id)].dose = dose
        self.vaccination_certificates[self.find_index_for_deletion(
            self.vaccination_certificates, id)].certificate_id = certificate_id

    def select_digital_certificates(self, query):
        return list(filter(lambda digital_cert: query.upper() in digital_cert.citizen.name.upper() + " " + digital_cert.citizen.surname.upper(), self.digital_certificates))

    def add_digital_certificate(self, digital_certificate):
        digital_certificate.id = self.global_id
        self.global_id += 1
        self.digital_certificates.append(digital_certificate)

    def delete_digital_certificate(self, id):
        self.digital_certificates.pop(
            self.find_index_for_deletion(self.digital_certificates, id))

    def edit_digital_certificate(self, id, citizen, certificate_id):
        self.digital_certificates[self.find_index_for_deletion(
            self.digital_certificates, id)].citizen = citizen
        self.digital_certificates[self.find_index_for_deletion(
            self.digital_certificates, id)].certificate_id = certificate_id

    def sort_data(self):
        self.citizens.sort(
            key=lambda citizen: citizen.surname + " " + citizen.name)
        self.medical_workers.sort(
            key=lambda medical_worker: medical_worker.surname + " " + medical_worker.name)
        self.vaccines.sort(key=lambda vaccine: vaccine.expire_date)
        self.vaccination_certificates.sort(
            key=lambda certificate: certificate.issuance_date)
        self.doses.sort(key=lambda dose: dose.dosage_date)
        self.digital_certificates.sort(
            key=lambda digita_certificate: digita_certificate.issuance_date)

    def save_data(self):
        filehandler = open('data', 'wb')
        pickle.dump(self, filehandler)
        filehandler.close()

    def load_data(self):
        filehandler = open('data', 'rb')
        loaded_data = pickle.load(filehandler)
        self.global_id = loaded_data.global_id
        self.citizens = loaded_data.citizens
        self.vaccines = loaded_data.vaccines
        self.medical_workers = loaded_data.medical_workers
        self.vaccination_certificates = loaded_data.vaccination_certificates
        self.digital_certificates = loaded_data.digital_certificates
        self.doses = loaded_data.doses
        filehandler.close()

    def __init__(self) -> None:
        self.global_id = 0
        self.citizens = []
        self.medical_workers = []
        self.vaccines = []
        self.vaccination_certificates = []
        self.digital_certificates = []
        self.doses = []

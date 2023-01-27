from Citizen import Citizen
from DigitacCertificate import DigitalCertificate
from Dose import Dose
from MedicalWorker import MedicalWorker
from VaccinationCertificate import VaccinationCertificate
from Vaccine import Vaccine
from Data import Data
from datetime import date

# test


def test():

    citizen = Citizen("1234567890123", "John", "Doe",
                      date(2000, 3, 3), "male", "1234567890")
    medical_worker = MedicalWorker(
        "1234567890122", "Jane", "Doe", date(1999, 3, 3), "female", "Leeman")

    vaccine = Vaccine("Phizer", "1234567890", "USA", date.today())
    dose = Dose(date(2016, 3, 3), vaccine,
                medical_worker, citizen, "Serbia")

    vacc_cert = VaccinationCertificate("12345678", date(
        2021, 10, 10), dose, citizen, medical_worker)

    citizen.vaccination_certificates.append(vacc_cert)
    citizen.doses_received.append(dose)
    citizen.digital_certificate = DigitalCertificate(
        "12345678", date(2000, 1, 1), citizen)

    data = Data()
    data.load_data()
    print(data.citizens[0])


"""data.edit_citizen(6, Citizen("1234567890987", "Jo", "Jo",
                      date(1999, 9, 9), 'male', '1234567890')) """


"""     print(data.citizens[0])
    print("_______________________")
    print(data.medical_workers[0])
    print("_______________________")
    print(data.doses[0])
    print("_______________________")
    print(data.digital_certificates[0].id)
    print("_______________________")
    print(data.vaccination_certificates[0])
    print("_______________________")
    print(data.vaccines[0].id) """


"""
    data.load_data()
    data.delete_citizen(0)
    data.delete_medical_worker(3)
    data.delete_dose(4)
    data.delete_vaccination_certificate(5)
    data.delete_digital_certificate(2)
    data.delete_vaccine(1) """


test()

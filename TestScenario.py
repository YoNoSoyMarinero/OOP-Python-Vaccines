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
    # citizen = Citizen("1234567890123", "John", "Doe",
    #                   date(2000, 3, 3), "male", "1234567890")
    # medical_worker = MedicalWorker(
    #     "1234567890122", "Jane", "Doe", date(1999, 3, 3), "female", "Leeman")

    # vaccine = Vaccine("Phizer", "1234567890", "USA", date.today())
    # dose = Dose(date(2016, 3, 3), vaccine,
    #             medical_worker, citizen, "Serbia")

    # vacc_cert = VaccinationCertificate("12345678", date(
    #     2021, 10, 10), dose, citizen, medical_worker)

    # citizen.vaccination_certificates.append(vacc_cert)
    # citizen.doses_received.append(dose)
    # citizen.digital_certificate = DigitalCertificate(
    #     "12345678", date(2000, 1, 1), citizen)

    data = Data()

    # data.add_citizen(citizen)
    # data.add_medical_worker(medical_worker)
    # data.add_dose(dose)
    # data.add_digital_certificate(citizen.digital_certificate)
    # data.add_vaccination_certificate(vacc_cert)
    # data.add_vaccine(vaccine)

    data.load_data()
    data.save_data()


test()

from datetime import date


class VaccinationCertificate:

    @property
    def issuance_date(self):
        return self.__issuance_date

    @property
    def citizen(self):
        return self.__citizen

    @citizen.setter
    def citizen(self, citizen):
        self.__citizen = citizen

    @property
    def medical_worker(self):
        return self.__medical_worker

    @medical_worker.setter
    def medical_worker(self, medical_worker):
        self.__medical_worker = medical_worker

    @property
    def dose(self):
        return self.__dose

    @dose.setter
    def dose(self, dose):
        self.__dose = dose

    @issuance_date.setter
    def issuance_date(self, issuance_date):
        if (not self.issuance_date_validation(issuance_date)):
            raise ValueError("Issuance date was unvalid!")
        else:
            self.__issuance_date = issuance_date

    @property
    def certificate_id(self):
        return self.__certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        if (not self.certificate_id_validation(certificate_id)):
            raise ValueError("ID was unvalid!")
        else:
            self.__certificate_id = certificate_id

    def issuance_date_validation(self, issuance_date):
        return issuance_date < date.today()

    def certificate_id_validation(self, certificate_id):
        return len(certificate_id) == 1

    def constructor_validation(self, certificate_id, issuance_date):
        if (not self.issuance_date_validation(issuance_date)):
            raise ValueError("Issuance date was unvalid!")
        if (not self.certificate_id_validation(certificate_id)):
            raise ValueError("ID was unvalid!")

    def __init__(self, certificate_id, issuance_date, dose, citizen, medica_worker) -> None:
        self.constructor_validation(certificate_id, issuance_date)
        self.id = None
        self.__certificate_id = certificate_id
        self.__issuance_date = issuance_date
        self.__dose = dose
        self.__citizen = citizen
        self.__medical_worker = medica_worker

    def __str__(self) -> str:
        return "Certificate id:{}\nIssuance date:{}\nDose:{}\nCitizen:{} {}\nMedical worker:{} {}".format(self.certificate_id, self.issuance_date, self.__dose.vaccine.name, self.__citizen.name, self.__citizen.surname, self.__medical_worker.name, self.__medical_worker.name, self.__medical_worker.surname)

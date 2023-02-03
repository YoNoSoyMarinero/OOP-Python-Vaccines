from datetime import date


class DigitalCertificate:

    @property
    def certificate_id(self):
        return self.__certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        if (not self.certificate_id_validation(certificate_id)):
            raise ValueError("ID was unvalid!")
        else:
            self.__certificate_id = certificate_id

    @property
    def citizen(self):
        return self.__citizen

    @citizen.setter
    def citizen(self, citizen):
        self.__citizen = citizen

    @property
    def issuance_date(self):
        return self.__issuance_date

    @issuance_date.setter
    def issuance_date(self, issuance_date):
        if (not self.issuance_date_validation(issuance_date)):
            raise ValueError("Issuance date was unvalid!")
        else:
            self.__issuance_date = issuance_date

    def certificate_id_validation(self, certificate_id):
        return len(certificate_id) == 1

    def issuance_date_validation(self, issuance_date):
        return issuance_date < date.today()

    def constructor_validation(self, certificate_id, issuance_date):
        if (not self.issuance_date_validation(issuance_date)):
            raise ValueError("Issuance date was unvalid!")
        if (not self.certificate_id_validation(certificate_id)):
            raise ValueError("ID was unvalid!")

    def __init__(self, certificate_id, issuance_date, citizen):
        self.constructor_validation(certificate_id, issuance_date)
        self.id = None
        self.__certificate_id = certificate_id
        self.__issuance_date = issuance_date
        self.__citizen = citizen

    def __str__(self) -> str:
        return "ID:{}\nIssuance date:{}\nCitizen:{} {}".format(self.certificate_id, self.issuance_date, self.__citizen.name, self.__citizen.surname)

from Person import Person


class Citizen(Person):

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, id_number):
        if (not self.id_number_validation(id_number)):
            raise ValueError("ID number was unvalid!")
        else:
            self.__id_number = id_number

    @property
    def digital_certificate(self):
        return self.__digital_certificate

    @digital_certificate.setter
    def digital_certificate(self, digital_certificate):
        self.__digital_certificate = digital_certificate

    @property
    def vaccination_certificates(self):
        return self.__vaccination_certificates

    @property
    def doses_received(self):
        return self.__doses_received

    def id_number_validation(self, id_number):
        return len(id_number) == 1

    def constructor_validation_citizen(self, id_number):
        if (not self.id_number_validation(id_number)):
            raise ValueError("ID number was unvalid!")

    def show_doses(self):
        print("___________________________________________________")
        for dose in self.doses_received:
            print(dose)
            print("___________________________________________________")

    def show_vaccination_certificates(self):
        print("___________________________________________________")
        for dose in self.vaccination_certificates:
            print(dose)
            print("___________________________________________________")

    def add_dose(self, dose):
        self.doses_received.append(dose)

    def add_vaccination_certificate(self, vaccination_certificate):
        self.vaccination_certificates.append(vaccination_certificate)

    def __init__(self, JMBG, name, surname, date_of_birth, sex, id_number) -> None:
        super().__init__(JMBG, name, surname, date_of_birth, sex)

        self.constructor_validation_citizen(id_number)
        self.id = None
        self.__id_number = id_number
        self.__doses_received = []
        self.__vaccination_certificates = []
        self.__digital_certificate = None

    def __str__(self):
        return "JMBG:{}\nName:{}\nSurname:{}\nBirthday:{}\nSex:{}\nID:{}".format(self.JMBG, self.name, self.surname, self.date_of_birth, self.sex, self.id_number)

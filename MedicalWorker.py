from Person import Person
from datetime import date


class MedicalWorker(Person):
    @property
    def health_institution(self):
        return self.__health_institution

    @health_institution.setter
    def health_institution(self, health_institution):
        if (not self.health_institution_validation(health_institution)):
            raise ValueError("Health institution was unvalid!")
        else:
            self.__health_institution = health_institution

    def health_institution_validation(self, health_institution):
        return len(health_institution) > 1

    def constructor_validation_medical_worker(self, health_institution):
        if (not self.health_institution_validation(health_institution)):
            raise ValueError("Health institution was unvalid!")

    def __init__(self, JMBG, name, surname, date_of_birth, sex, health_institution) -> None:
        super().__init__(JMBG, name, surname, date_of_birth, sex)

        self.constructor_validation_medical_worker(health_institution)
        self.id = None
        self.__health_institution = health_institution

    def __str__(self):
        return "JMBG:{}\nName:{}\nSurname:{}\nBirthday:{}\nSex:{}\nHealth institution:{}".format(self.JMBG, self.name, self.surname, self.date_of_birth, self.sex, self.health_institution)

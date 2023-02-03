from datetime import date


class Dose:

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        if (not self.country_validation(country)):
            raise ValueError("Country institution was unvalid!")
        else:
            self.__country = country

    @property
    def dosage_date(self):
        return self.__dosage_date

    @dosage_date.setter
    def dosage_date(self, dosage_date):
        if (not self.dosage_date_validation(dosage_date)):
            raise ValueError("Date was unvalid!")
        else:
            self.__dosage_date = dosage_date

    def country_validation(self, country):
        return len(country) > 1

    def dosage_date_validation(self, dosage_date):
        return dosage_date < date.today()

    def constructor_validation(self, dosage_date, country):
        if (not self.dosage_date_validation(dosage_date)):
            raise ValueError("Date was unvalid!")
        if (not self.country_validation(country)):
            raise ValueError("Country was unvalid!")

    def __init__(self, dosage_date, vaccine, medical_worker, citizen, country) -> None:
        self.constructor_validation(dosage_date, country)
        self.id = None
        self.__dosage_date = dosage_date
        self.vaccine = vaccine
        self.medical_worker = medical_worker
        self.citizen = citizen
        self.__country = country

    def __str__(self) -> str:
        return "Dosage date:{}\nVaccine:{}\nMedical worker:{} {}\nCitizen:{} {}\nCountry:{}".format(self.dosage_date, self.vaccine.name, self.medical_worker.name, self.medical_worker.surname, self.citizen.name, self.citizen.surname, self.country)

from datetime import date


class Vaccine:

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if (not self.name_validation(name)):
            raise ValueError("Name was unvalid!")
        else:
            self.__name = name

    @property
    def serial_number(self):
        return self.__serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        if (not self.serial_number_validation(serial_number)):
            raise ValueError("Serial number was unvalid!")
        else:
            self.__serial_number = serial_number

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        if (not self.country_validation(country)):
            raise ValueError("Country was unvalid!")
        else:
            self.__country = country

    @property
    def expire_date(self):
        return self.__expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        self.__expire_date = expire_date

    def name_validation(self, name):
        return len(name) > 1

    def serial_number_validation(self, serial_number):
        return len(serial_number) == 1

    def country_validation(self, country):
        return len(country) > 1

    def vaccine_constructor_validation(self, name, serial_number, country):
        if (not self.name_validation(name)):
            raise ValueError("Name was unvalid!")
        if (not self.serial_number_validation(serial_number)):
            raise ValueError("Serial number was unvalid!")
        if (not self.country_validation(country)):
            raise ValueError("Country was unvalid!")

    def __init__(self, name, serial_number, country, expire_date) -> None:
        self.vaccine_constructor_validation(name, serial_number, country)
        self.id = None
        self.__name = name
        self.__serial_number = serial_number
        self.__country = country
        self.__expire_date = expire_date

    def __str__(self) -> str:
        return "Name:{}\nSerial number:{}\nCountry:{}\nExpire date:{}".format(self.name, self.serial_number, self.country, self.expire_date)

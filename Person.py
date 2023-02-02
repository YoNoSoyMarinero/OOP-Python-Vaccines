from datetime import date


class Person:

    @property
    def JMBG(self):
        return self.__JMBG

    @JMBG.setter
    def JMBG(self, JMBG):
        if (not self.JMBG_validation(JMBG)):
            raise ValueError("JMBG was unvalid!")
        else:
            self.__JMBG = JMBG

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
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if (not self.surname_validation(surname)):
            raise ValueError("Surname was unvalid!")
        else:
            self.__surname = surname

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        if (not self.date_of_birth_validation(date_of_birth)):
            raise ValueError("Date of birth was unvalid!")
        else:
            self.__date_of_birth = date_of_birth

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if (not self.sex_validation(sex)):
            raise ValueError("Sex must be f or m!")
        else:
            self.__sex = sex

    def JMBG_validation(self, JMBG):
        return len(JMBG) == 1

    def name_validation(self, name):
        return len(name) > 1

    def surname_validation(self, surname):
        return len(surname) > 1

    def date_of_birth_validation(self, date):
        return date < date.today()

    def sex_validation(self, sex):
        return sex == 'm' or sex == 'f'

    def constructor_validation(self, JMBG, name, surname, date_of_birth, sex):
        if (not self.JMBG_validation(JMBG)):
            raise ValueError("JMBG was unvalid!")
        if (not self.name_validation(name)):
            raise ValueError("Name was unvalid!")
        if (not self.surname_validation(surname)):
            raise ValueError("Surname was unvalid!")
        if (not self.date_of_birth_validation(date_of_birth)):
            raise ValueError("Date of birth was unvalid!")
        if (not self.sex_validation(sex)):
            raise ValueError("Sex must be f or m!")

    def __init__(self, JMBG, name, surname, date_of_birth, sex) -> None:
        self.constructor_validation(JMBG, name, surname, date_of_birth, sex)
        self.__JMBG = JMBG
        self.__name = name
        self.__surname = surname
        self.__date_of_birth = date_of_birth
        self.__sex = sex

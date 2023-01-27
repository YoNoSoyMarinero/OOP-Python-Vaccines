from Person import Person
from datetime import date


try:
    person1 = Person("1234567890123", 'John', 'Mal', date(1999, 3, 9), 'male')
    person2 = Person("1244567890123", 'Peter', 'Bel', date(1998, 9, 9), 'male')
    persons = [person1, person2]
    query = "Peter"

    queried_index = None
    for index in range(len(persons)):
        if persons[index].JMBG == "1234567890123":
            queried_index = index
            break

    persons.pop(index)

    persons.sort(key=lambda person: person.date_of_birth)
    for person in persons:
        print(person.surname)

    queried_persons = list(filter(lambda person: query.upper(
    ) in person.surname.upper() + " " + person.name.upper(), persons))


except Exception as e:
    print(e)

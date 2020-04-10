from datetime import datetime
class Student:
    def __init__(self, firstName, lastName, birth_year):
        self._name = firstName + " " + lastName
        self._birth_year = birth_year

if __name__ == '__main__':
    s = Student("Rob", "Everest", 1961)
    years_old = datetime.now().year - s._birth_year
    print(f"{s._name} is {years_old} old")

class teacher():
    def __init__(self, name, age, vacationdays, subject):
        self.name = name
        self.age = age
        self.vacationdays = vacationdays
        self.subject = subject

    def __str__(self):
        return self.name + " is " + str(self.age) + " years old and has " + str(self.vacationdays) + " vacation days." \
                         " He teaches " + self.subject + "."


class math_teacher(teacher):
    def __init__(self, name, age, vacationdays, subject, specialization):
        super().__init__(name, age, vacationdays, subject)
        self.subject = subject
        self.specialization = specialization

    def __str__(self):
        return super().__str__() + " He is good at " + self.specialization + "."


class programming_teacher(teacher):
    def __init__(self, name, age, vacationdays, subject, favorite_language):
        super().__init__(name, age, vacationdays, subject)
        self.favorite_language = favorite_language

    def __str__(self):
        return super().__str__() + " He loves the Programminglanguage " + self.favorite_language + "."

class german_teacher(teacher):
    def __init__(self, name, age, vacationdays, subject, favorite_author):
        super().__init__(name, age, vacationdays, subject)
        self.favorite_author = favorite_author

    def __str__(self):
        return super().__str__() + " He likes to read Books from " + self.favorite_author + "."

def main():
    wischonig = math_teacher("Wischonig", 19, 84, "Math", "Glieder")
    rubner = programming_teacher("Rubner", 19, 84, "Programming", "Python")
    daxer = german_teacher("Daxer", 19, 84, "German", "Kafka")

    print(wischonig)
    print(rubner)
    print(daxer)

if __name__ == "__main__":
    main()
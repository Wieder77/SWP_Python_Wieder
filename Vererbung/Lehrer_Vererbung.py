class teacher():
    def __init__(self, name, age, vacationdays, subject):
        # C) neuer Fehler NICHT behebar
        if name is None:
            raise ValueError("Der Leherer muss einen Namen haben!")
        self.name = name
        # A) neuer Fehler und behebar
        if age < 0:
            self.age = 0
        else:
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
        if favorite_language is None:
            self.favorite_language = "Python"
        else:
            self.favorite_language = favorite_language

    def __str__(self):
        return super().__str__() + " He loves the Programminglanguage " + self.favorite_language + "."

class german_teacher(teacher):
    def __init__(self, name, age, vacationdays, subject, favorite_author):
        super().__init__(name, age, vacationdays, subject)
        self.favorite_author = favorite_author

    def __str__(self):
        return super().__str__() + " He likes to read Books from " + self.favorite_author + "."

def teacher_age_10years(teacher):
    return int(teacher.age) + 10


def main():
    wischonig = math_teacher("Wischonig", 19, 84, "Math", "Glieder")
    rubner = programming_teacher("Rubner", 19, 84, "Programming", "Python")
    daxer = german_teacher("Daxer", 19, 84, "German", "Kafka")

    print(wischonig)
    print(rubner)
    print(daxer)

    # A) neuer Fehler und behebar
    a_lehrer = teacher("TestLehrerA", -1, 84, "German")
    print(a_lehrer)
    # B)hochblubber-Fehler und behebar
    b_lehrer = programming_teacher("TestLehrerB", 19, 84, "Programming", None)
    print(b_lehrer)
    # C) neuer Fehler NICHT behebar
    # c_lehrer = teacher(None, 19, 84, "German")
    # D) hochblubber-Fehler und NICHT behebar
    # d_lehrer = german_teacher("TestLehrerD", None, 84, "German", None)
    # print(teacher_age_10years(d_lehrer))




if __name__ == "__main__":
    main()  
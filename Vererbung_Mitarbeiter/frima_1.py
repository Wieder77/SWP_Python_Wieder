import enum

class Gender(enum.Enum):
    male = "male"
    female = "female"

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        if not isinstance(gender, Gender):
            return "The gender is not valid."
        self.gender = gender

class Department():
    def __init__(self, department_name, employees, department_manager):
        self.department_name = department_name
        self.employees = employees
        self.department_manager = department_manager


class Employee(Person):
    def __init__(self, name, age, gender, salary):
        Person.__init__(self, name, age, gender)
        self.salary = salary


class Department_manager(Employee):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender, salary)


class Company():
    def __init__(self, company_name, departements):
        self.name = company_name
        self.departements = departements

    def count_employees(self):
        count_employees, count_manageres = 0, 0
        for department in self.departements:
            count_employees = count_employees + len(department.employees)
            count_manageres = count_manageres + 1
        return count_employees, count_manageres

    def count_departments(self):
        return len(self.departements)

    def department_with_most_employees(self):
        employee_number = {}
        for department in self.departements:
            employee_number[department] = len(department.employees)
        return str(max(employee_number, key=employee_number.get).department_name)

    def women_percentage(self):
        female_employees = 0
        male_employees = 0
        for department in self.departements:
            for employee in department.employees:
                if employee.gender.value == "female":
                    female_employees += 1
                else:
                    male_employees += 1
            total_employees = female_employees + male_employees
        return (female_employees / total_employees) * 100


def main():
    employee1 = Employee("Fritz1", 19, Gender.male, 50000)
    employee = Employee("Fritz", 19, Gender.male, 50000)
    employee2 = Employee("Fritz", 19, Gender.female, 50000)
    manager1 = Department_manager("Hans", 19,Gender.female, 50000)
    it = Department("IT", [employee1, employee,employee2], manager1)
    ad = Department("AD", [employee1, employee], manager1)
    company1 = Company("Google", [it, ad])
    # zählt mitarbeiter sowie manager
    print(company1.count_employees())
    #zählt departements
    print(company1.count_departments())
    # meisten mitarbeiter in abteilung
    print(company1.department_with_most_employees())
    # prozentualer anteil von frauen
    print(company1.women_percentage())

if __name__ == "__main__":
    main()

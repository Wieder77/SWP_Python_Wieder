class Auto:
    def __init__(self, ps):
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return f"Beide Autos haben zusmmen {self.ps + other.ps} PS."
        else:
            return "Fehler!"

    def __sub__(self, other):
        if isinstance(other, Auto):
            return f"Beide Autos abgezogen voneinander {self.ps - other.ps} PS."
        else:
            return "Fehler!"

    def __mul__(self, other):
        if isinstance(other, Auto):
            return f"Beide Autos multipliziert miteinander {self.ps * other.ps} PS."
        else:
            return "Fehler!"

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        else:
            return "Fehler!"

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        else:
            return "Fehler!"

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        else:
            return "Fehler!"


    def __str__(self):
        return f"Das Auto hat {self.ps:.2f} PS."


if __name__ == "__main__":
    auto1 = Auto(100)
    print(auto1)
    auto2 = Auto(200)
    print(auto2)
    # Add
    print(auto1 + auto2)
    # Sub
    print(auto1 - auto2)
    # Mul
    print(auto1 * auto2)

    # Vergleiche
    # Gleich
    print(auto1 == auto2)
    # Größer
    print(auto1 > auto2)
    # Kleiner
    print(auto1 < auto2)

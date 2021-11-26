
class Fractie(object):

    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.get_numarator()}/{self.get_numitor()}"

    def __add__(self, fractie):
        self.veirificare_numitor(fractie)

        if(fractie.get_numitor() == self.get_numitor()):
            return Fractie(self.get_numarator() + fractie.get_numarator(), self.get_numitor())
        else:
            numarator = self.get_numarator() * fractie.get_numitor() + \
                fractie.get_numarator() * self.get_numitor()
            numitor = self.get_numitor() * fractie.get_numitor()
            return Fractie(numarator, numitor)

    def __sub__(self, fractie):
        self.veirificare_numitor(fractie)

        if(fractie.get_numitor() == self.get_numitor()):
            return Fractie(self.get_numarator() - fractie.get_numarator(), self.get_numitor())
        else:
            numarator = self.get_numarator() * fractie.get_numitor() - \
                fractie.get_numarator() * self.get_numitor()
            numitor = self.get_numitor() * fractie.get_numitor()
            return Fractie(numarator, numitor)

    def inverse(self):
        return Fractie(self.get_numitor(), self.get_numarator())

    def veirificare_numitor(self, fractie):
        """ Verifica ca numitorul sa nu fie 0"""
        if(self.get_numitor() == 0 or fractie.get_numitor() == 0):
            raise Exception("Numitorul este 0!")

    def set_numarator(self, numarator):
        self.numarator = numarator

    def get_numarator(self):
        return self.numarator

    def get_numitor(self):
        return self.numitor

    def set_numitor(self, numitor):
        self.numitor = numitor


if __name__ == "__main__":
    f1 = Fractie(5, 3)
    f2 = Fractie(4, 2)
    f3 = f1 + f2
    inversaF3 = f3.inverse()
    print(f"{f1} + {f2} = {f3}")
    print(f"Inversa {f3} = {inversaF3}")
    print(f"{f1} - {inversaF3} = {f1 - inversaF3}")

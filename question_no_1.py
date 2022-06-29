# Create a class programmer for storing informations of a few programmars working in microsoft

class Programmar:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(
            f"The name of the {self.company} programmar is {self.name} amd the product is {self.product}.")


ayan = Programmar("Ayan", "Amazon")
ishita = Programmar("Ishita", "Google")

ayan.getInfo()
ishita.getInfo()

class Railwayform:
    formType = "RailwayForm"
    def printData (self):
        print(f"Name is {self.name}.")
        print(f"Train is {self.train}.")
ayansApplication = Railwayform()
ayansApplication.name = "Ayan"
ayansApplication.train = "Rajdhani Express"
ayansApplication.printData()
# Write a class train which has methods to book a ticket, get status(no of seats)and get fare information of trains
# remaining under Indian railways

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print("*********************")
        print(f"The name of the train is {self.name}.")
        print(f"The seats available in the train are {self.seats}.")
        print("**********************")

    def fareInfo(self):
        print(
            f'The price of the ticket of Intercity Express is Rs. {self.fare}/-')

    def bookTicket(self):

        if(self.seats > 0):

            print(
                f"Your ticket has been booked,\n your seat number is {self.seats}")
            self.seats = self.seats - 1

        else:
            print("Sorry! This train is full, kindly try tatkal")

    def cancelticket(self, seatNo):
        pass


intercity = Train("Intercity Express - 14015", 90, 2)
intercity.getstatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.getstatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getstatus()


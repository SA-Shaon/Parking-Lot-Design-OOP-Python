"""
    Parking Lot Design uing Python OOP 

1. Display spots available on parking lot.
2. Park their car in the parking lot and get ticket.
3.Remove car from parking lot.
    Ticket, 1hour --> 5tk 20hour++ --> 50tk


Classes:
    Car -->
        license
        model
        color
    Garage -->
        spot available
        add car
        remove 
        show car
"""


class Car:
    def __init__(self, license, model, color):
        self.license = license
        self.model = model
        self.color = color

    def __repr__(self):
        return f"{self.license}, {self.model}, {self.color}"


"""
    __repr__  = formal string, not readable
    str(__repr__) = readable formate string

    another way to readable string return 
    def __str__(self):
        return f"{self.license}, {self.model}, {self.color}
"""


class Garage:
    def __init__(self):
        self.car_added = []
        self.spot = 10
        self.car_infos = {}
        self.bill = 0
        self.ticket = []

    def spots_available(self):
        return self.spot

    def add_car_to_garage(self, car):
        self.spot_name = ['A1', 'B1', 'C1', 'D1',
                          'E1', 'F1', 'G1', 'H1', 'I1', 'J1']
        if self.spots_available() > 0:
            user_data = str(car).split(', ')
            self.spot -= 1
            self.car_added.append(user_data)
            self.car_infos = {'Tickets': [],
                              'License': [], 'Model': [], 'Color': []}
            ticket = ""
            for i, val in enumerate(self.car_added):
                ticket = self.spot_name[i]+user_data[0]
                self.car_infos['Tickets'].append(ticket)
                self.car_infos['License'].append(val[0])
                self.car_infos['Model'].append(val[1])
                self.car_infos['Color'].append(val[2])

            print(f"Successfully Parked!!! Your Ticket {ticket}")
        else:
            print("No Spots Available!!")

    def unpark(self, ticket, hours):
        past_spot_len = len(self.car_infos['Tickets'])
        if ticket not in self.car_infos['Tickets']:
            print("NO CAR FOUND!!!!!")
        else:
            for i, val in enumerate(self.car_infos['Tickets']):
                if val == ticket:
                    print(f"YOUR LICENSE IS {self.car_infos['License'][i]}")
                    print(f"YOUR MODEL IS {self.car_infos['Model'][i]}")
                    print(f"YOUR COLOR IS {self.car_infos['Color'][i]}")
                    removed_car_index = i
                    # Delete unpark car user data
                    self.car_infos['License'].pop(i)
                    self.car_infos['Tickets'].pop(i)
                    self.car_infos['Model'].pop(i)
                    self.car_infos['Color'].pop(i)
                    self.spot += 1


my_garage = Garage()
my_car = Car('4568DM', 'Audi', 'Black')
my_garage.add_car_to_garage(my_car)
my_garage.unpark('A14568DM', 2)

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

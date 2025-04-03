class Vehicle():
    def __init__ (self,mark:str,model:str):
        self.mark = mark
        self.model = model
    def Type_Fuel (self,fuel:str):
        fuel = 'Type Unknow'
        print (fuel)

    def Capacity_Passengers (self,passengers:int):
        passengers = 0
        print (f'Will bord {passengers} passengers')





class Car (Vehicle):
    def __init__(self, mark: str, model: str,):
        super().__init__(mark, model)



    def Type_Fuel(self, fuel: str):
        if fuel == 'Gasoline':
            return print (f'Added {fuel}')
        else:
            print("This Car don't accept this type of fuel, just Gasoline")



    def Capacity_Passengers (self,passengers:int):
        if passengers > 5:
            print ('This Car dont support more that 5 passengers!')
        elif passengers <= 0:
            print (f'there is no way to board {passengers} passengers')
        else:
            print (f'Will board {passengers} passengers')



    def InfoCar (self):
        return print (f'This Car are of the mark {self.mark}, model {self.model}, and just accepts Gasoline in type of fuel, and support in maxime 5 passengers')
    




class MotorBike (Vehicle):
    def __init__(self, mark:str, model:str):
        super().__init__(mark, model)



    def Type_Fuel(self, fuel: str):
        if fuel == 'Gasoline':
            return print(f'Added {fuel}')
        else:
            print("This MotorBike don't accept this type of fuel, just Gasoline")



    def Capacity_Passengers (self,passengers:int):
        if passengers > 2:
            print ('This MotorBike dont support more that 2 passengers!')
        elif passengers <= 0:
            print (f'there is no way to board {passengers} passengers')
        else:
            print (f'Will board {passengers} passengers')



    def InfoMotorBike (self):
        return print (f'This MotorBike are of the mark {self.mark}, model {self.model}, and just accepts Gasoline in type of fuel, and support in maxime 2 passengers')
    






class Truck(Vehicle):
    def __init__(self, mark:str, model:str):
        super().__init__(mark, model)

    def Type_Fuel(self, fuel: str):
        if fuel == 'Diesel':
            return  print(f'Added {fuel}')

        else:
            print("This Truck don't accept this type of fuel, just Diesel")



    def Capacity_Passengers (self,passengers:int):
        if passengers > 2:
            print ('This Truck dont support more that 2 passengers!')
        elif passengers <= 0:
            print (f'there is no way to board {passengers} passengers')
        else:
            print (f'Will board {passengers} passengers')



    def InfoTruck (self):
        return print (f'This Truck are of the mark {self.mark}, model {self.model}, and just accepts Diesel in type of fuel, and support in maxime 2 passengers')

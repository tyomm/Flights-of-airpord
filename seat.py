class Seat:
    def __init__(self, number, status):
        self._number = number
        self._status = status

#========Getters=======
    def Get_number(self):
        return self._number

    def Get_status(self):
        return self._status

#========Setters=======
    def Set_number(self, number):
        self._number = number

    def Set_status(self, status):
        self._status = status


#========Property method========
    number = property(Get_number, Set_number)
    status = property(Get_status, Set_status)


#========Show info function=======
    def Show_info(self):
        print("number -->", self._number, "\n", "status -->", self._status, "\n" "=================== ")


seat1 = Seat("1", "busy")
seat2 =  Seat("2", "busy")
seat3 = Seat("3", "free")
seat4 = Seat("4", "busy")
seat5 = Seat("5", "busy")
seat6 = Seat("6", "busy")
seat7 = Seat("7", "busy")
seat8 = Seat("8", "busy")
seat9 = Seat("9", "free")
seat10 = Seat("10", "busy")
seat11 = Seat("11", "busy")
seat12 = Seat("12", "free")
seat13 = Seat("13", "free")
seat14 = Seat("14", "busy")
seat15 = Seat("15", "busy")
seat16 = Seat("16", "busy")
seat17 = Seat("17", "busy")
seat18 = Seat("18", "free")
seat19 = Seat("19", "busy")
seat20 = Seat("20", "busy")

list_for_objects = [seat1, seat2, seat3, seat4, seat5, seat6, seat7, seat8, seat9, seat10, seat11, seat12, seat13, seat14, seat15, seat16, seat17, seat18, seat19, seat20]

def Seat_final_function():
    for i in range(len(list_for_objects)):
        x = list_for_objects[i].Show_info()
    return x

# Seat_final_function()

# Finished
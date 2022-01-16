from seat import *
from passenger import *
from country import *

class Ticket:
    def __init__(self, from_, to, id, passenger_name, price, seat_number, max_kg):
        self._from_ = from_
        self._to = to
        self._id = id
        self._passenger_name = passenger_name
        self._price = price
        self._seat_number = seat_number
        self._max_kg = max_kg


#========Getters=======
    def Get_from_(self):
        return self._from_

    def Get_to(self):
        return self._to

    def Get_id(self):
        return self._id

    def Get_passenger_name(self):
        return self._passenger_name

    def Get_price(self):
        return self._price

    def Get_seat_number(self):
        return self._seat_number

    def Get_max_kg(self):
        return self._max_kg

#========Setters=======
    def Set_from_(self, from_):
        self._from_ = from_

    def Set_to(self, to):
        self._to = to

    def Set_id(self, id):
        self._id = id

    def Set_passenger_name(self, passenger_name):
        self._passenger_name = passenger_name

    def Set_price(self, price):
        self._price = price

    def Set_seat_number(self, seat_number):
        self._seat_number = seat_number

    def Set_max_kg(self, max_kg):
        self._max_kg = max_kg

#========Property method========
    from_ = property(Get_from_, Set_from_)
    to = property(Get_to, Set_to)
    id = property(Get_id, Set_id)
    passenger_name = property(Get_passenger_name, Set_passenger_name)
    price = property(Get_price, Set_price)
    seat_number = property(Get_seat_number, Set_seat_number)
    max_kg = property(Get_max_kg, Set_max_kg)


# ========Show info function=======
    def Show_info(self):

        while True:   
            list_ticket_info = [self._from_, self._to, self._id, self._passenger_name, self._price, self._seat_number, self._max_kg]
            enter_ticket_info = input("\n Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n (from_, to, id, passenger_name, price, seat_number, max_kg) \n")

            for i in range(len(list_ticket_info)):
                
                list_nick_ticket = {"from_": "from_", "to": "to", "id": "id", "passenger_name": "passenger_name", "price": "price", "seat_number": "seat_number", "max_kg": "max_kg"}
                
                if enter_ticket_info == "from_":
                    print("Wich country he's comeing to --> ", self.from_.name)
                    break
                if enter_ticket_info == "to":
                    print("Where he's going to --> ", self.to.name)
                    break
                if enter_ticket_info == "id":
                    print("Ticket id --> ", self.id)
                    break
                if enter_ticket_info == "passenger_name":
                    print("Name and surname -->", self.passenger_name.name, self.passenger_name.surname)
                    break
                if enter_ticket_info == "price":
                    print("Price --> ", self.price)
                    break
                if enter_ticket_info == "seat_number":
                    print("Seat number --> ", self.seat_number.number)
                    break
                if enter_ticket_info == "max_kg":
                    print("Max kg for baggage --> ", self.max_kg)
                    break
            if enter_ticket_info == "end":
                break
#============================================================
            x = 0
            while x == 0:
                if enter_ticket_info == list_nick_ticket["from_"]:
                    if enter_ticket_info == list_nick_ticket["from_"]:
                        x += 1
                        break
                if enter_ticket_info == list_nick_ticket["to"]:
                    if enter_ticket_info == list_nick_ticket["to"]:
                        x += 1
                        break
                if enter_ticket_info == list_nick_ticket["id"]:
                    if enter_ticket_info == list_nick_ticket["id"]:
                        x += 1
                        break
                if enter_ticket_info == list_nick_ticket["passenger_name"]:
                    if enter_ticket_info == list_nick_ticket["passenger_name"]:
                        x += 1
                        break
                if enter_ticket_info == list_nick_ticket["price"]:
                    if enter_ticket_info == list_nick_ticket["price"]:
                        x += 1
                        break
                if enter_ticket_info == list_nick_ticket["seat_number"]:
                    if enter_ticket_info == list_nick_ticket["seat_number"]:
                        x += 1
                        break
                if enter_ticket_info == list_nick_ticket["max_kg"]:
                    if enter_ticket_info == list_nick_ticket["max_kg"]:
                        x += 1
                        break
                print("Ops: Not found")
                break


ticket1 = Ticket(Armenia, France, "017896", pass1, "300$", seat1, "30kg")
ticket2 = Ticket(Armenia, Austria, "014567", pass2, "180$", seat2, "25kg")
ticket3 = Ticket(Germany, Armenia, "014557", pass3, "210$", seat4, "20kg")
ticket4 = Ticket(Armenia, Spain, "018947", pass4, "250$", seat5, "26kg")
ticket5 = Ticket(Netherlands, Armenia, "013546", pass5, "170$", seat6, "28kg")



list_ticket = {"ticket1": ticket1, "ticket2": ticket2, "ticket3": ticket3, "ticket4": ticket4, "ticket5": ticket5}

def show_result(l_ticket):
    for i in range(len(l_ticket)):
        choose_ticket = input("Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n (ticket1, ticket2, ticket3, ticket4, ticket5) --> ")
        if choose_ticket == "ticket1":
            l_ticket["ticket1"].Show_info() 
        elif choose_ticket == "ticket2":  
            l_ticket["ticket2"].Show_info()
        elif choose_ticket == "ticket3":  
            l_ticket["ticket3"].Show_info()
        elif choose_ticket == "ticket4":  
            l_ticket["ticket4"].Show_info()
        elif choose_ticket == "ticket5":  
            l_ticket["ticket5"].Show_info()
        else:
            break


def Ticket_final_function():
    return show_result(list_ticket)
 

# Ticket_final_function()

# Finished


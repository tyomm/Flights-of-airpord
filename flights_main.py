from airplane import *
from passenger import *
from country import *
from city import *
from airport import *
from payment import *
from pilot import *
from seat import *
from ticket import *
from flight import *


what_do_you_want = input("Pls choose one of the specified parameters \n  see_info, add, search (If you want to stop the query, enter 'end')\n" )

if what_do_you_want == "see_info":
    while True:
        print("========================================================================== \n Flights information: ")
        info = input("Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n  --> (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) <-- \n 1) --> Passenger info \n 2) --> Country info \n 3) --> Airplane info \n 4) --> City info \n 5) --> Airport info \n 6) --> Flight info \n 7) --> Payment info \n 8) --> Pilot info \n 9) --> Seat info \n 10) --> Ticket info \n =================== \n" )


        if info == "1":
            print("Passenger info:")
            Passenger_final_function()  # Passenger
            
        elif info == "2":
            print("Country info:")
            Country_final_function()    # Country
        elif info == "3":
            print("Airplane info:")
            Airplane_final_function()   # Airplane
        elif info == "4":
            print("City info:")
            City_final_function()   # City
        elif info == "5":
            print("Airport info:")
            Airport_final_function()    # Airport

        elif info == "6":
            print("Flight info:")  #  # Flight
            Flight_final_function() 
        
        elif info == "7":
            print("Payment info:")
            Payment_final_function() # Payment

        elif info == "8":
            print("Pilot info:")
            Pilot_final_function() # Pilot
            
        elif info == "9":
            print("Seat info:")
            Seat_final_function()   # Seat

        elif info == "10":
            print("Ticket info:")  #ticket
            Ticket_final_function()
        if info == "end":
            break
            

#=============Creating ADD function================
def ADD ():

    if what_do_you_want == "add":
        choose_class = int(input("Pls choose one of the specified parameters \n 1) --> Airplane class, \n 2) --> Airport class, \n 3) --> City class, \n 4) --> Country class, \n 5) --> Flight class, \n 6) --> Passenger class, \n 7) --> Payment class, \n 8) --> Pilot class, \n  9) --> Seat class, \n 10) --> Ticket_class \n --> "))
        
        # choose_class_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        # 1) --> Airplane class
        # 2) --> Airport class 
        # 3) --> City class
        # 4) --> Country class 
        # 5) --> Flight class
        # 6) --> Passenger class
        # 7) --> Payment class
        # 8) --> Pilot class
        # 9) --> Seat class
        # 10) --> Ticket_class
  
        while True:
            continue_or_end = input("\n <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!> \n (.: If you want to stop the query, enter 'end' :. \n .: if you want to stay on this class enter 'stay' :.\n .: if you want to choose other class please enter 'choose' :. )\n --> ") 
            
            if continue_or_end == "end":
                break
            # Stay Airplane class
            elif continue_or_end == "stay":
                choose_class = choose_class  # stay on classes
            elif continue_or_end == "choose":
                ADD()
                break
        
            while True:
                # For Airplane class
                if choose_class == 1:           # Choosing class from all program
                    print("You can add something on Airplane class")
                    add_input_object = input("Add object --> ")
                    if add_input_object == "end":
                        break
                    print_object_name = add_input_object
                    #airplane_code, airplane_model
                    print("\n Add atributs on", add_input_object)
                    add_input_atrubut1 = input("(Enter airplane_model) --> ")
                    if add_input_atrubut1 == "end":
                        break
                    add_input_atrubut2 = input("(Enter airplane_model) --> ")
                    if add_input_atrubut2 == "end":
                        break
                    add_input_object = Airplane(add_input_atrubut1, add_input_atrubut2)
                    print(".:", add_input_object.airplane_code,",", add_input_object.airplane_model, ":.", "are ", "'", print_object_name,"'",  " object atributs \n")
                    break
                # For Airport class
                if choose_class == 2:           # Choosing class for all program
                    print("You can add something on Airport class")
                    add_input_object = input("Add object --> ")
                    if add_input_object == "end":
                        break
                    print_object_name = add_input_object
                    #id, name, country, city, phone, email, website
                    print("\n Add atributs on", add_input_object)
                    add_input_atrubut1 = input("(Enter id)  --> ")
                    if add_input_atrubut1 == "end":
                        break
                    add_input_atrubut2 = input("(Enter name) --> ")
                    if add_input_atrubut2 == "end":
                        break
                    add_input_atrubut3 = input("Enter country --> ")
                    if add_input_atrubut3 == "end":
                        break
                    add_input_atrubut4 = input("Enter city --> " )
                    if add_input_atrubut4 == "end":
                        break
                    add_input_atrubut5 = input("Enter phone --> ")
                    if add_input_atrubut5 == "end":
                        break
                    add_input_atrubut6 = input("Enter email -->")
                    if add_input_atrubut6 == "end":
                        break
                    add_input_atrubut7 = input("Enter website --> ")
                    if add_input_atrubut7 == "end":
                        break
                    add_input_object = Airport(add_input_atrubut1, add_input_atrubut2, add_input_atrubut3, add_input_atrubut4, add_input_atrubut5, add_input_atrubut6, add_input_atrubut7)
                    print(".:", add_input_object.id,",", add_input_object.name,",", add_input_object.country,",", add_input_object.city,",", add_input_object.phone,",", add_input_object.email,",", add_input_object.website, ":.", "are ", "'", print_object_name,"'",  " object atributs \n")
                    break
                # For City class 
                if choose_class == 3:           # Choosing class from all program
                    print("You can add something on City class")
                    add_input_object = input("Add object --> ")
                    if add_input_object == "end":
                                    break
                    print_object_name = add_input_object
                    # location_lng, location_ltd, name, country
                    print("\n Add atributs on", add_input_object)
                    add_input_atrubut1 = input("(Enter location_lng)  --> ")
                    if add_input_atrubut1 == "end":
                        break
                    add_input_atrubut2 = input("(Enter location_ltd) --> ")
                    if add_input_atrubut2 == "end":                      
                        break

                    add_input_atrubut3 = input("(Enter city name) --> ")
                    if add_input_atrubut3 == "end":
                        break
                    add_input_atrubut4 = input("(Enter country) --> ")
                    if add_input_atrubut4 == "end":
                        break
                    add_input_object = City(add_input_atrubut1, add_input_atrubut2, add_input_atrubut3, add_input_atrubut4)
                    print(".:", add_input_object.location_lng,",", add_input_object.location_ltd,",", add_input_object.name,",", add_input_object.country, ":.", "are ", "'", print_object_name,"'",  " object atributs \n")
                    break
                # For Country class
                if choose_class == 4:           # Choosing class from all program
                    print("You can add something on Country class")
                    add_input_object = input("Add object --> ")
                    if add_input_object == "end":
                        break
                    print_object_name = add_input_object
                    # name, location_ltd, location_lng
                    print("\n Add atributs on", add_input_object)
                    add_input_atrubut1 = input("(Enter country name)  --> ")
                    if add_input_atrubut1 == "end":
                        break
                    add_input_atrubut2 = input("(Enter location_ltd) --> ")
                    if add_input_atrubut2 == "end":
                        break
                    add_input_atrubut3 = input("(Enter location_lng) --> ")
                    if add_input_atrubut3 == "end":
                        break
                    add_input_object = Country(add_input_atrubut1, add_input_atrubut2, add_input_atrubut3)
                    print(".:", add_input_object.name,",", add_input_object.location_ltd,",", add_input_object.location_lng, ":.", "are ", "'", print_object_name,"'",  " object atributs \n")
                    break
                # For Flight class
                if choose_class == 5:           # Choosing class for all program
                    print("You can add something on Flight class")
                    add_input_object = input("Add object --> ")
                    if add_input_object == "end":
                        break
                    print_object_name = add_input_object
                    # from_airport_id, to_airport_id, departure_time, arrival_time, departure_date,  duration,  air_plane
                    print("\n Add atributs on", add_input_object)
                    add_input_atrubut1 = input("(Enter from_airport_id)  --> ")
                    if add_input_atrubut1 == "end":
                        break
                    add_input_atrubut2 = input("(Enter to_airport_id) --> ")
                    if add_input_atrubut2 == "end":
                        break
                    add_input_atrubut3 = input("Enter departure_time --> ")

                    if add_input_atrubut3 == "end":
                        break
                    add_input_atrubut4 = input("Enter arrival_time --> " )
                    if add_input_atrubut4 == "end":
                        break
                    add_input_atrubut5 = input("Enter departure_date --> ")
                    if add_input_atrubut5 == "end":
                        break
                    add_input_atrubut6 = input("Enter duration -->")
                    if add_input_atrubut6 == "end":
                        break
                    add_input_atrubut7 = input("Enter air_plane --> ")
                    if add_input_atrubut7 == "end":
                        break
                    add_input_object = Flight(add_input_atrubut1, add_input_atrubut2, add_input_atrubut3, add_input_atrubut4, add_input_atrubut5, add_input_atrubut6, add_input_atrubut7)
                    print(".:", add_input_object.from_airport_id,",", add_input_object.to_airport_id,",", add_input_object.departure_time,",", add_input_object.arrival_time,",", add_input_object.departure_date,",", add_input_object.duration,",", add_input_object.air_plane, ":.", "are ", "'", print_object_name,"'",  " object atributs \n")
                    break
                # For Passenger class
                if choose_class == 6:           # Choosing class for all program
                    print("You can add something on Passenger class")
                    add_input_object = input("Add object --> ")
                    add_input_object
                    print_object_name = add_input_object
                    # name, surname, age, mobile, email, adress
                    print("\n Add atributs on", add_input_object)
                    add_input_atrubut1 = input("(Enter passenger name)  --> ")
                    if add_input_atrubut1 == "end":
                        break
                    add_input_atrubut2 = input("(Enter passenger surname) --> ")
                    if add_input_atrubut2 == "end":
                        break
                    add_input_atrubut3 = input("Enter passenger age --> ")
                    if add_input_atrubut3 == "end":
                        break
                    add_input_atrubut4 = input("Enter passenger mobile --> " )
                    if add_input_atrubut4 == "end":
                        break
                    add_input_atrubut5 = input("Enter passenger email --> ")
                    if add_input_atrubut5 == "end":
                        break
                    add_input_atrubut6 = input("Enter passenger adress -->")
                    if add_input_atrubut6 == "end":
                        break
                    add_input_object = Passenger(add_input_atrubut1, add_input_atrubut2, add_input_atrubut3, add_input_atrubut4, add_input_atrubut5, add_input_atrubut6)
                    print(".:", add_input_object.name,",", add_input_object.surname,",", add_input_object.age,",", add_input_object.mobile,",", add_input_object.email,",", add_input_object.adress, ":.", "are ", "'", print_object_name,"'",  " object atributs \n")
                    break
                # For Payment class
                if choose_class == 7:           # Choosing class from all program
                    print("You can add something on Payment class")
                    add_input_object = input("Add object --> ")
                    if add_input_object == "end":
                        break
                    print_object_name = add_input_object
                    # credit_card_id, username
                    print("\n Add atributs on", add_input_object)
                    add_input_atrubut1 = input("(Enter credit_card_id)  --> ")
                    if add_input_atrubut1 == "end":
                        break
                    add_input_atrubut2 = input("(Enter username and name) --> ")
                    if add_input_atrubut2 == "end":
                        break
                    add_input_object = Payment(add_input_atrubut1, add_input_atrubut2)
                    print(".:", add_input_object.credit_card_id,",", add_input_object.username, ":.", "are ", "'", print_object_name,"'",  " object atributs \n")
                    break
                # For Pilot class
                if choose_class == 8:           # Choosing class from all program
                    print("You can add something on Pilot class")
                    add_input_object = input("Add object --> ")
                    if add_input_object == "end":
                        break
                    print_object_name = add_input_object
                    # name, phone, adress, email
                    print("\n Add atributs on", add_input_object)
                    add_input_atrubut1 = input("(Enter name)  --> ")
                    if add_input_atrubut1 == "end":
                        break
                    add_input_atrubut2 = input("(Enter phone) --> ")
                    if add_input_atrubut2 == "end":
                        break
                    add_input_atrubut3 = input("(Enter adress) --> ")
                    if add_input_atrubut3 == "end":
                        break
                    add_input_atrubut4 = input("(Enter email) --> ")
                    if add_input_atrubut4 == "end":
                        break
                    add_input_object = Pilot(add_input_atrubut1, add_input_atrubut2, add_input_atrubut3, add_input_atrubut4)
                    print(".:", add_input_object.name,",", add_input_object.phone,",", add_input_object.adress,",", add_input_object.email, ":.", "are ", "'", print_object_name,"'",  " object atributs \n")
                    break
                # For Seat class
                if choose_class == 9:           # Choosing class from all program
                    print("You can add something on Seat class")
                    add_input_object = input("Add object --> ")
                    if add_input_object == "end":
                        break
                    print_object_name = add_input_object
                    # number, status
                    print("\n Add atributs on", add_input_object)
                    add_input_atrubut1 = input("(Enter number)  --> ")
                    if add_input_atrubut1 == "end":
                        break
                    add_input_atrubut2 = input("(Enter status) --> ")
                    if add_input_atrubut2 == "end":
                        break
                    add_input_object = Seat(add_input_atrubut1, add_input_atrubut2)
                    print(".:", add_input_object.number,",", add_input_object.status, ":.", "are ", "'", print_object_name,"'",  " object atributs \n")
                    break
                # For Ticket class
                if choose_class == 10:           # Choosing class for all program
                    print("You can add something on Ticket class (If you want to stop the query, enter 'end')")
                    add_input_object = input("Add object --> ")
                    if add_input_object == "end":
                        break
                    print_object_name = add_input_object
                    # from_, to, id, passenger_name, price, seat_number, max_kg
                    print("\n Add atributs on", add_input_object)
                    add_input_atrubut1 = input("(Enter from_)  --> ")
                    if add_input_atrubut1 == "end":
                        break
                    add_input_atrubut2 = input("(Enter to) --> ")
                    if add_input_atrubut2 == "end":
                        break
                    add_input_atrubut3 = input("Enter id --> ")
                    if add_input_atrubut3 == "end":
                        break
                    add_input_atrubut4 = input("Enter passenger_name --> " )
                    if add_input_atrubut4 == "end":
                        break
                    add_input_atrubut5 = input("Enter price --> ")
                    if add_input_atrubut5 == "end":
                        break
                    add_input_atrubut6 = input("Enter seat_number -->")
                    if add_input_atrubut6 == "end":
                        break
                    add_input_atrubut7 = input("Enter max_kg --> ")
                    if add_input_atrubut7 == "end":
                        break
                    add_input_object = Ticket(add_input_atrubut1, add_input_atrubut2, add_input_atrubut3, add_input_atrubut4, add_input_atrubut5, add_input_atrubut6, add_input_atrubut7)
                    print(".:", add_input_object.from_,",", add_input_object.to,",", add_input_object.id,",", add_input_object.passenger_name,",", add_input_object.price,",", add_input_object.seat_number,",", add_input_object.max_kg, ":.", "are ", "'", print_object_name,"'",  " object atributs \n")
                    break

#=================Createing Search function==============
# def Search():
#    pass

ADD()


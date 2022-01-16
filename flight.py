from typing import Pattern
from airplane import *
from airport import *

class Flight:
    def __init__(self, from_airport_id, to_airport_id, departure_time, arrival_time, departure_date,  duration,  air_plane) -> None:
        self._from_airport_id = from_airport_id
        self._to_airport_id = to_airport_id
        self._departure_time = departure_time
        self._arrival_time = arrival_time
        self._departure_date = departure_date
        self._duration = duration
        self._air_plane = air_plane
        

#=======Getters=======

    def Get_from_airport_id(self):
        return self._from_airport_id

    def Get_to_airport_id(self):
        return self._to_airport_id

    def Get_departure_time(self):
        return self._departure_time

    def Get_arrival_time(self):
        return self._arrival_time

    def Get_departure_date(self):
        return self._departure_date

    def Get_duration(self):
        return self._duration 

    def Get_air_plane(self):
        return self._air_plane

#=======Setters=======

    def Set_from_airport_id(self, from_airport_id):
        self._from_airport_id = from_airport_id

    def Set_to_airport_id(self, to_airport_id):
        self._to_airport_id = to_airport_id

    def Set_departure_time(self, departure_time):
        self._departure_time = departure_time

    def Set_arrival_time(self, arrival_time):
        self._arrival_time = arrival_time

    def Set_departure_date(self, departure_date):
        self._departure_date = departure_date

    def Set_duration(self, duration):
        self._duration = duration

    def Set_air_plane(self, air_plane):
        self._air_plane = air_plane

#========Property method=======
    from_airport_id = property(Get_from_airport_id, Set_from_airport_id)
    to_airport_id = property(Get_to_airport_id, Set_to_airport_id)
    departure_time = property(Get_departure_time, Set_departure_time)
    arrival_time = property(Get_arrival_time, Set_arrival_time)
    departure_date = property(Get_departure_date, Set_departure_date)
    duration = property(Get_duration, Set_duration)
    air_plane = property(Get_air_plane, Set_air_plane)


#========Show info function=======
    def Show_info(self):
        print("From airport id -->", self._from_airport_id.id, "\n", "To airport id -->", self._to_airport_id.id, "\n", 
                                    "Departure time -->", self._departure_time, "\n", "Arrival time -->", self._arrival_time, "\n",  
                                    "Departure date -->", self._departure_date, "\n",  "Duration -->", self._duration, "\n",  "Airplane code and model -->", self._air_plane.airplane_code, ", ", self._air_plane.airplane_model,  "\n ================================================ \n", ) 
                                    

print("================================================= \n")
# Flight objects
Flight1 = Flight(Evn, Cdg, "19:00", "21:00", "13.10.2021", "2 hours", airplane1)
Flight2 = Flight(Evn, Vie, "01:30", "03:00", "9.10.2021", "2 hours, 30 minutes", airplane2)
Flight3 = Flight(Sxf, Evn, "12:00", "01:00", "16.10.2021", "1 hour", airplane3)
Flight4 = Flight(Evn, Mad, "17:00", "20:00", "12.10.2021", "3 hours", airplane1)
Flight5 = Flight(Ams, Evn, "22:00", "23:30", "07.10.2021", "1 hour, 30 minutes", airplane2)


flight_objects_list = [Flight1, Flight2, Flight3, Flight4, Flight5]

def Flight_final_function():
    for i in range(len(flight_objects_list)):
        x = flight_objects_list[i].Show_info()
    return x


# Flight_final_function()

# Finished
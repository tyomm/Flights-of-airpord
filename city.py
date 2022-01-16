from country import *

class City:
    def __init__(self, location_lng, location_ltd, name, country) -> None:
        self._location_lng = location_lng
        self._location_ltd = location_ltd
        self._name = name
        self._country = country
    

#========Getters===========
    def Get_location_lng(self):
        return self._location_lng

    def Get_location_ltd(self):
        return self._location_ltd

    def Get_name(self):
        return self._name

    def Get_country (self):
        return self._country
    
   
#===========Setters===========
    def Set_location_lng (self, location_lng):
        self._location_lng = location_lng
    
    def Set_location_ltd(self, location_ltd):
        self._location_ltd = location_ltd

    def Set_name (self, name):
        self._name = name

    def Set_country (self, country):
        self._country = country    

#========Property method=======
    location_lng = property(Get_location_lng, Set_location_lng)
    location_ltd = property(Get_location_ltd, Set_location_ltd)
    name = property(Get_name, Set_name)
    country = property(Get_country, Set_country)

#========Show info function=======
    def Show_info(self):

        while True:                  
            list_city_info = [self._location_lng, self._location_ltd, self._name, self._country]
            enter_city_info = input("\n Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n (location_lng, location_ltd, name, country) \n")

            for i in range(len(list_city_info)):
                
                list_nick_city = {"loc_lng": "location_lng", "loc_ltd": "location_ltd", "na": "name", "cou": "country"}


                if enter_city_info == "location_lng":
                    print("Location longitude --> ", self._location_lng)
                    break
                if enter_city_info == "location_ltd":
                    print("location latitude --> ", self._location_ltd)
                    break
                if enter_city_info == "name":
                    print("name --> ", self._name)
                    break
                if enter_city_info == "country":
                    print("name -->", self._country.name, "\n", "location latitude --> ", self._country.location_ltd, "\n", "location longitude-->", self._country.location_lng, "\n")  
                    break
            if enter_city_info == "end":
                break

#============================================================
            x = 0
            while x == 0:
                if enter_city_info == list_nick_city["loc_lng"]:
                    if enter_city_info == list_nick_city["loc_lng"]:
                        x += 1
                        break
                if enter_city_info == list_nick_city["loc_ltd"]:
                    if enter_city_info == list_nick_city["loc_ltd"]:
                        x += 1
                        break
                if enter_city_info == list_nick_city["na"]:
                    if enter_city_info == list_nick_city["na"]:
                        x += 1
                        break
                if enter_city_info == list_nick_city["cou"]:
                    if enter_city_info == list_nick_city["cou"]:
                        x += 1
                        break
                print("Ops: Not found")
                break

# City objects
city1 = City("40.179188", "44.499104", "Yerevan", Armenia)
city2 = City("48.848691", "2.347856", "Paris", France)
city3 = City("48.2082", "16.3738", "Vienna", Austria)
city4 = City("52.5200", "13.4050", "Berlin", Germany)
city5 = City("40.4160", "3.7038", "Madrid", Spain)
city6 = City("52.3676", "4.9041", "Amsterdam", Netherlands )


# location_lng, location_ltd, name, country




list_city = {"Yerevan": city1, "Paris": city2, "Vienna": city3, "Berlin": city4, "Madrid": city5, "Amsterdam": city6}

def show_result(l_city):
    for i in range(len(l_city)):
        choose_city = input("Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n (Yerevan, Paris, Vienna, Berlin, Madrid, Amsterdam) \n -->  ")
        if choose_city == "Yerevan":
            l_city["Yerevan"].Show_info() 
            break
        if choose_city == "Paris":
            l_city["Paris"].Show_info() 
            break
        
        if choose_city == "Vienna":
            l_city["Vienna"].Show_info() 
            break
        if choose_city == "Berlin":
            l_city["Berlin"].Show_info() 
            break
        if choose_city == "Madrid":
            l_city["Madrid"].Show_info() 
            break
        if choose_city == "Amsterdam":
            l_city["Amsterdam"].Show_info() 
            break

def City_final_function():
    return show_result(list_city)


# City_final_function()

# Finished




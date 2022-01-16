from city import *
from country import *

class Airport:
    
    def __init__(self, id, name, country, city, phone, email, website) -> None:
        
        self.id = id
        self._name = name
        self._country = country
        self._city = city
        self._phone = phone
        self._email = email
        self._website = website
        
#========Getters=========
    def Get_id(self):
        return self._id

    def Get_name(self):
        return self._name

    def Get_country(self):
        return self._country

    def Get_city(self):
        return self._city

    def Get_phone(self):
        return self._phone

    def Get_email(self):
        return self._email

    def Get_website(self):
        return self._website

    

#=======Setters=========
    def Set_id(self, id):
        self._id = id

    def Set_name(self, name):
        self._name = name

    def Set_country(self, country):
        self._country = country

    def Set_city(self, city):
        self._city = city

    def Set_phone(self, phone):
        self._phone = phone

    def Set_email(self, email):
        self._email = email

    def Set_website(self, website):
        self._website = website
     
    

#========Property method=======
    id = property(Get_id, Set_id)
    name = property(Get_name, Set_name)
    country = property(Get_country, Set_country)
    city = property(Get_city, Set_city)
    phone = property(Get_phone, Set_phone)
    email = property(Get_email, Set_email)
    website = property(Get_website, Set_website)
    
#========Show info function=======
    def Show_info(self):
        
        while True:
            enter_airport_info = input("\n Pls enter one of the specified parArmeniaeters (If you want to stop the query, enter 'end') \n (id, name, country, city, phone, email, website) \n")
            list_airport_info = [self._id, self._name, self._country, self._city, self._phone, self._email, self._website]
            
            for i in range(len(list_airport_info)):
                
                list_nick_airport = {"id": "id", "name": "name", "country": "country", "city": "city", "phone": "phone", "email": "email", "website": "website"}
                
                if enter_airport_info == "id":
                    print("id --> ", self._id)
                    break
                if enter_airport_info == "name":
                    print("name --> ", self._name)
                    break
                if enter_airport_info == "country":
                    print("country --> ", self._country.name)
                    break
                if enter_airport_info == "city":
                    print("city -->", self._city.name)
                    break
                if enter_airport_info == "phone":
                    print("phone --> ", self._phone)
                    break
                if enter_airport_info == "email":
                    print("email --> ", self._email)
                    break
                if enter_airport_info == "website":
                    print("website --> ", self._website)
                    break
            if enter_airport_info == "end":
                break

#============================================================
            x = 0
            while x == 0:
                if enter_airport_info == list_nick_airport["id"]:
                    if enter_airport_info == list_nick_airport["id"]:
                        x += 1
                        break
                if enter_airport_info == list_nick_airport["name"]:
                    if enter_airport_info == list_nick_airport["name"]:
                        x += 1
                        break
                if enter_airport_info == list_nick_airport["country"]:
                    if enter_airport_info == list_nick_airport["country"]:
                        x += 1
                        break
                if enter_airport_info == list_nick_airport["city"]:
                    if enter_airport_info == list_nick_airport["city"]:
                        x += 1
                        break
                if enter_airport_info == list_nick_airport["phone"]:
                    if enter_airport_info == list_nick_airport["phone"]:
                        x += 1
                        break
                if enter_airport_info == list_nick_airport["email"]:
                    if enter_airport_info == list_nick_airport["email"]:
                        x += 1
                        break
                if enter_airport_info == list_nick_airport["website"]:
                    if enter_airport_info == list_nick_airport["website"]:
                        x += 1
                        break
                print("Ops: Not found")
                break

# Airport objects
Evn = Airport("Evn", "Zvartnoc", Armenia, city1, "010 49 30 00", "contacts@aia-zvartnots.aero", "http://www.zvartnots.aero" )
Cdg = Airport("Cdg", "Charles de Gaulle", France, city2, "+1 800-237-2747", "...", "https://wwws.airfrance.us/")
Vie = Airport("Vie", "Vienna International Airport", Austria, city3, "+43 1 70070", "info@Viennaairport.com", "https://www.Viennaairport.com/")
Sxf = Airport("Sxf", "Berlin Schönefeld Airport", Germany, city4, "+49 30 60911150", "...", "https://ber.berlin-airport.de/")
Mad = Airport("Mad", "Barajas Adolfo Suárez", Spain, city5, "+34 913 21 10 00", "clientesMad@aena.es", "https://www.aeropuertoMadrid-barajas.com/")
Ams = Airport("Ams", "Amsterdam Airport Schiphol", Netherlands, city6, "+31 900 7244 7465", "...", "https://www.schiphol.nl/")


list_airport = {"Zvartnots": Evn}

def show_result(l_city):
    for i in range(len(l_city)):
        choose_airport = input("Pls enter one of the specified parArmeniaeters (If you want to stop the query, enter 'end') \n (Zvartnots) \n -->  ")
        if choose_airport == "Zvartnots":
            l_city["Zvartnots"].Show_info() 

            break

def Airport_final_function():
    return show_result(list_airport)


# Airport_final_function()

# Finished







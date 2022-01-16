class Country:
    def __init__(self,  name, location_ltd, location_lng) -> None:
        self._name = name
        self._location_ltd =location_ltd
        self._location_lng = location_lng

#========Getters========
    def Get_name(self):
        return self._name
    
    def Get_location_ltd(self):
        return self._location_ltd
    
    def Get_location_lng(self):
        return self._location_lng
    
#=======Setters=========
    def Set_name(self, name):
        self._name = name

    def Set_location_ltd(self, location_ltd):
        self._location_ltd = location_ltd

    def Set_location_lng(self, location_lng):
        self._location_lng = location_lng

    
#========Property method=======
    name = property(Get_name, Set_name)
    location_ltd = property(Get_location_ltd, Set_location_ltd)
    location_lng = property(Get_location_lng, Set_location_lng)
    


#========Show info function=======
    def Show_info(self):
        print("name -->", self._name, "\n", "Latitude -->", self._location_ltd, "\n", "Longitude -->", self._location_lng, "\n====================" )

# Country objects
Armenia = Country( "Armenia", "40.069099", "45.038189") # From/To  
France = Country("France", "46.227638", "2.213749")     # To   
Austria = Country("Austria", "47.5162", "14.5501") # To      =
Germany = Country("Germany", "51.1657", "10.4515") # From #  
Spain = Country("Spain", "40.4637", "3.7492") # To
Netherlands = Country("Netherlands", "52.1326", "5.2913") # From


country_objects_list = [Armenia, France, Austria, Germany, Spain, Netherlands]

def Country_final_function():
    for i in range(len(country_objects_list)):
        x = country_objects_list[i].Show_info()
    return x

# Country_final_function()

# Finished
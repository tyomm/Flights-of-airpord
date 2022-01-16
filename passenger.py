class Passenger:
    def __init__(self, name, surname, age, mobile, email, adress) -> None:
        self._name = name
        self._surname = surname
        self._age = age
        self._mobile = mobile
        self._email = email
        self._adress = adress


#========Getters========
    def Get_name(self):
        return self._name

    def Get_surname(self):
        return self._surname

    def Get_age(self):
        return self._age

    def Get_mobile(self):
        return self._mobile

    def Get_email(self):
        return self._email

    def Get_adress(self):
        return self._adress

#========Setters========
    def Set_name(self, name):
        self._name = name

    def Set_surname(self, surname):
        self._surname = surname

    def Set_age(self, age):
        self._age = age

    def Set_mobile(self, mobile):
        self._mobile = mobile

    def Set_email(self, email):
        self._email = email

    def Set_adress(self, adress):
        self._adress = adress

#========Property method=======
    name = property(Get_name, Set_name)
    surname = property(Get_surname, Set_surname)
    age = property(Get_age, Set_age)
    mobile = property(Get_mobile, Set_mobile)
    email = property(Get_email, Set_email)
    adress = property(Get_adress, Set_adress)



#========Show info function=======
    def Show_info(self):

        while True:   
            list_pass_info = [self._name, self._surname, self._age, self._mobile, self._email, self._adress]
            enter_passenger_info = input("\n Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n (name, surname, age, mobile, email, adress) \n")

            for i in range(len(list_pass_info)):
                
                list_nick_passenger = {"na": "name", "su": "surname", "ag": "age", "mo": "mobile", "em": "email", "ad": "adress"}
                
                if enter_passenger_info == "name":
                    print("name --> ", self._name)
                    break
                if enter_passenger_info == "surname":
                    print("surname --> ", self._surname)
                    break
                if enter_passenger_info == "age":
                    print("age --> ", self._age)
                    break
                if enter_passenger_info == "mobile":
                    print("mobile -->", self._mobile)
                    break
                if enter_passenger_info == "email":
                    print("email --> ", self._email)
                    break
                if enter_passenger_info == "adress":
                    print("adress --> ", self._adress)
                    break
            if enter_passenger_info == "end":
                break
#============================================================
            x = 0
            while x == 0:
                if enter_passenger_info == list_nick_passenger["na"]:
                    if enter_passenger_info == list_nick_passenger["na"]:
                        x += 1
                        break
                if enter_passenger_info == list_nick_passenger["su"]:
                    if enter_passenger_info == list_nick_passenger["su"]:
                        x += 1
                        break
                if enter_passenger_info == list_nick_passenger["ag"]:
                    if enter_passenger_info == list_nick_passenger["ag"]:
                        x += 1
                        break
                if enter_passenger_info == list_nick_passenger["mo"]:
                    if enter_passenger_info == list_nick_passenger["mo"]:
                        x += 1
                        break
                if enter_passenger_info == list_nick_passenger["em"]:
                    if enter_passenger_info == list_nick_passenger["em"]:
                        x += 1
                        break
                if enter_passenger_info == list_nick_passenger["ad"]:
                    if enter_passenger_info == list_nick_passenger["ad"]:
                        x += 1
                        break
                print("Ops: Not found")
                break

# Passenger objects
pass1 = Passenger("Arsen",  "Harutyunyan", "26", "+374 55 65 77 51", "arsen.harutyunyan@gmail.com", "San Francisco (California, USA)")
pass2 = Passenger("Amelia", "Gharssayan", "19", "+37493 67 89 44", "Amelia-Gharssayan@gmail.com", "Erevan, (Armenia)")
pass3 = Passenger("Lusine", "Avetisyan", "21", "+374 91 09 76 45", "Lusin.avetisyan07@gmail.com", "Erevan, (Armenia)")
pass4 = Passenger("Harry", "Styles", "25", "+44 7911 123456", "Harry_chicken29@gmail.com", "London, (UK)")
pass5 = Passenger("Vasil", "Stepanyan", "35", "+1 437 484 279 256", "Stepanyan_Vasil@gmail.com", "Paris, (France)")

list_pass = {"p1": pass1, "p2": pass2, "p3": pass3, "p4": pass4}

def show_result(l_pass):
    for i in range(len(l_pass)):
        choose_pass = input("Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n (pass1, pass2, pass3, pass4) --> ")
        if choose_pass == "pass1":
            l_pass["p1"].Show_info() 
        elif choose_pass == "pass2":  
            l_pass["p2"].Show_info()
        elif choose_pass == "pass3":  
            l_pass["p3"].Show_info()
        elif choose_pass == "pass4":  
            l_pass["p4"].Show_info()
        else:
            break
        

def Passenger_final_function():
    return show_result(list_pass)

# Passenger_final_function()

#Finished
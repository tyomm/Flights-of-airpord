class Pilot:
  def __init__(self, name, phone, adress, email):
    self._name = name
    self._phone = phone
    self._adress = adress
    self._email = email

#========Getters=======
  def Get_name(self):
    return self._name

  def Get_phone(self):
    return self._phone

  def Get_adress(self):
    return self._adress

  def Get_email(self):
    return self._email

#========Setters=======
  def Set_name(self, name):
    self._name = name

  def Set_phone(self, phone):
    self._phone = phone

  def Set_adress(self, adress):
    self._adress = adress

  def Set_email(self, email):
    self._email = email

#========Property method========
  name = property(Get_name, Set_name)
  phone = property(Get_phone, Set_phone)
  adress = property(Get_adress, Set_adress)
  email = property(Get_email, Set_email)

#========Show info function=======
  def Show_info(self):
                           
    while True:
            
      list_pilot_info = [self._name, self._phone, self._adress, self._email]
      enter_pilot_info = input("\n Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n name, phone, adress, email) \n")


      for i in range(len(list_pilot_info)):
             
        list_nick_pilot = {"name": "name", "phone": "phone", "adress": "adress" , "email": "email"}

        if enter_pilot_info == "name":
          print("Name --> ", self.name)
          break
        if enter_pilot_info == "phone":
          print("Phone --> ", self.phone)
          break
        if enter_pilot_info == "adress":
          print("Adress --> ", self.adress)
          break
        if enter_pilot_info == "email":
          print("E-mail --> ", self.email)
          break               
      if enter_pilot_info == "end":
        break


#============================================================
      x = 0
      while x == 0:
        if enter_pilot_info == list_nick_pilot["name"]:
          if enter_pilot_info == list_nick_pilot["name"]:
            x += 1
            break
        if enter_pilot_info == list_nick_pilot["phone"]:
          if enter_pilot_info == list_nick_pilot["phone"]:
            x += 1
            break
        if enter_pilot_info == list_nick_pilot["adress"]:
          if enter_pilot_info == list_nick_pilot["adress"]:
            x += 1
            break
        if enter_pilot_info == list_nick_pilot["email"]:
          if enter_pilot_info == list_nick_pilot["email"]:
            x += 1
            break
        print("Ops: Not found")
        break

# name, phone, adress, email

# Pilot objects
pilot1 = Pilot("Lia Sargsyan", "+374 98-75-57", "Abovyan", "lia.sargsyan@mail.ru")
pilot2 = Pilot("John Nazaryans", "+374 41-12-67-35", "California", "John.Nazaryans@gmail.com")
pilot3 = Pilot("Taylor Hill", "+1 866-648-4023", "Fresno", "Taylor-Hill03@gmial.com")
pilot4 = Pilot("Vrej Aramyan", "+374 95-34-76-54", "Ashtarak", "Vrej.Aramyan98@gmail.com")

list_pilot = {"pilot1": pilot1, "pilot2": pilot2, "pilot3": pilot3, "pilot4": pilot4}

def show_result(l_pilot):
  for i in range(len(l_pilot)):
    choose_pilot = input("Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n (pilot1, pilot2, pilot3, pilot4)  -->  ")
      
    if choose_pilot == "pilot1":
      l_pilot["pilot1"].Show_info() 
    if choose_pilot == "pilot2":
      l_pilot["pilot2"].Show_info() 
    if choose_pilot == "pilot3":
      l_pilot["pilot3"].Show_info() 
    if choose_pilot == "pilot4":
      l_pilot["pilot4"].Show_info() 
    else:
      break

def Pilot_final_function():
  return show_result(list_pilot)

# Pilot_final_function()

# Finished
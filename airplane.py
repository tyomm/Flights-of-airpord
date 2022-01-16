class Airplane:
  def __init__(self, airplane_code, airplane_model):
    self._airplane_code = airplane_code
    self._airplane_model = airplane_model

#========Getters=======
  def Get_airplane_code(self):
    return self._airplane_code

  def Get_airplane_model(self):
    return self._airplane_model

#========Setters=======
  def Set_airplane_code(self, airplane_code):
    self._airplane_code = airplane_code

  def Set_airplane_model(self, airplane_model):
    self._airplane_model = airplane_model

#=========Property method========
  airplane_code = property(Get_airplane_code, Set_airplane_code)
  airplane_model = property(Get_airplane_model, Set_airplane_model)


# ========Show info function=======
  def Show_info(self):

    while True:
      enter_airplane_info = input("\n Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n (airplane_code, airplane_model) \n")
      list_airplane_info = [self._airplane_code, self._airplane_model]
          
      for i in range(len(list_airplane_info)):
            
        list_nick_airplane = {"ai_code": "airplane_code", "ai_model": "airplane_model"}
              
        if enter_airplane_info == "airplane_code":
          print("airplane_code --> ", self._airplane_code)
          break
        if enter_airplane_info == "airplane_model":
          print("airplane_model --> ", self._airplane_model)
          break
      if enter_airplane_info == "end":
        break
#============================================================
      x = 0
      while x == 0:
        if enter_airplane_info == list_nick_airplane["ai_code"]:
          if enter_airplane_info == list_nick_airplane["ai_code"]:
            x += 1
            break
        if enter_airplane_info == list_nick_airplane["ai_model"]:
          if enter_airplane_info == list_nick_airplane["ai_model"]:
            x += 1
            break
        print("Ops: Not found")
        break

# Airplane objects
airplane1 = Airplane("DA62", "Diamond DA62")
airplane2 = Airplane("4243A4", "777-3m0")
airplane3 = Airplane("76E314", "airbus-314")

list_airline = {"a1": airplane1, "a2": airplane2, "a3": airplane3}

def show_result(l_airplane):
    for i in range(len(l_airplane)):
        choose_airline = input("Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n (airplane1, airplane2, airplane3) --> ")
        if choose_airline == "airplane1":
            l_airplane["a1"].Show_info() 
        elif choose_airline == "airplane2":  
            l_airplane["a2"].Show_info()
        elif choose_airline == "airplane3":  
            l_airplane["a3"].Show_info()
        else:
            break
        

def Airplane_final_function():
    return show_result(list_airline)

# Airplane_final_function()

# Finished



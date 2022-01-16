from passenger import Passenger


class Payment:
    def __init__(self, credit_card_id, username) -> None:
        self._credit_card_id = credit_card_id
        self._username = username

#========Getters=======
    def Get_credit_card_id(self):
        return self._credit_card_id

    def Get_username(self):
        return self._username

#========Setters=======
    def Set_credit_card_id(self, credit_card_id):
        self._credit_card_id = credit_card_id

    def Set_username(self, username):
        self._username = username

#========Property method=======

    credit_card_id = property(Get_credit_card_id, Set_credit_card_id)
    username = property(Get_username, Set_username)

#========Show info function=======
    def Show_info(self):
                           
        while True:
            
            list_payment_info = [self._credit_card_id, self._username]
            enter_payment_info = input("\n Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n credit_card_id, username) \n")


            for i in range(len(list_payment_info)):
             
                list_nick_payment = {"credit_card_id": "credit_card_id", "username": "username"}

                if enter_payment_info == "credit_card_id":
                    print("Credit card id --> ", self.credit_card_id)
                    break
                if enter_payment_info == "username":
                    print("Username --> ", self.username)
                    break
            if enter_payment_info == "end":
                break

#============================================================
            x = 0
            while x == 0:
                if enter_payment_info == list_nick_payment["credit_card_id"]:
                    if enter_payment_info == list_nick_payment["credit_card_id"]:
                        x += 1
                        break
                if enter_payment_info == list_nick_payment["username"]:
                    if enter_payment_info == list_nick_payment["username"]:
                        x += 1
                        break
                print("Ops: Not found")
                break


# Payment objects
pay1 = Payment("1777234", "Arsen Harutyunyan")
pay2 = Payment("1987645", "Amelia Gharssayan")
pay3 = Payment("1786354", "Lusine Avetisyan")
pay4 = Payment("1834753", "Harry Styles")
pay5 = Payment("1293748", "Vasil Stepanyan")

list_payment = {"payment1": pay1, "payment2": pay2, "payment3": pay3, "payment4": pay4}

def show_result(l_payment):
    for i in range(len(l_payment)):
        choose_person_payment = input("Pls enter one of the specified parameters (If you want to stop the query, enter 'end') \n (payment1, payment2, payment3, payment4, payment5)  -->  ")
        if choose_person_payment == "payment1":
            l_payment["payment1"].Show_info() 
        if choose_person_payment == "payment2":
            l_payment["payment2"].Show_info() 
        if choose_person_payment == "payment3":
            l_payment["payment3"].Show_info() 
        if choose_person_payment == "payment4":
            l_payment["payment5"].Show_info() 
        if choose_person_payment == "payment4":
            l_payment["payment5"].Show_info() 
        else:
            break

def Payment_final_function():
    return show_result(list_payment)

# Payment_final_function()

# Finished

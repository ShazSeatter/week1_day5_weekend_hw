# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop): 
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, money):
    if money > 0:
        pet_shop["admin"]["total_cash"] += money
     

# def missing here 

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, pets_sold):
   pet_shop["admin"]["pets_sold"] += pets_sold


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
    

# def get_pets_by_breed(pet_shop, breed):


def find_pet_by_name(pet_shop, name):
   for pet_name in pet_shop["pets"]:
    if pet_name["name"] == name:
        return pet_name


# def remove_pet_by_name(pet_shop, name):
#    pet_shop["pets"][3]["name"].remove(name)


def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash
    
            


            




    

# basically this function can be reuseable for other breeds if we want to look up
# how many (so a count) of that specified breed is in the pet shop 

# print(get_pets_by_breed(self.cc_pet_shop, "British Shorthair")

# print(get_pets_by_breed(self.cc_pet_shop, "Dalmation")


# what is the function called?
# what parameters does it need?
# what does the function need to return?
# what does the function need to do?



